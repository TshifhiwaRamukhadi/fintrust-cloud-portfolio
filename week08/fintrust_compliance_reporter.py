import boto3
import csv
import time


class FinTrustComplianceReporter:

    def __init__(
            self,
            database,
            output_bucket,
            region="af-south-1"):

        self.database = database

        self.output_bucket = output_bucket

        self.athena = boto3.client(
            "athena",
            region_name=region
        )

        self.s3 = boto3.client(
            "s3",
            region_name=region
        )

    def run_report(
            self,
            report_name,
            sql):

        response = (
            self.athena.start_query_execution(
                QueryString=sql,
                QueryExecutionContext={
                    "Database":
                        self.database
                },
                ResultConfiguration={
                    "OutputLocation":
                        f"s3://"
                        f"{self.output_bucket}/"
                        f"athena-results/"
                }
            )
        )

        query_id = response[
            "QueryExecutionId"
        ]

        while True:

            status = (
                self.athena.get_query_execution(
                    QueryExecutionId=query_id
                )
            )

            state = (
                status["QueryExecution"]
                      ["Status"]
                      ["State"]
            )

            if state in (
                "SUCCEEDED",
                "FAILED",
                "CANCELLED"
            ):
                break

            time.sleep(1)

        if state != "SUCCEEDED":
            raise RuntimeError(
                f"Query failed: {state}"
            )

        rows = (
            self.athena.get_query_results(
                QueryExecutionId=query_id
            )
        )["ResultSet"]["Rows"]

        csv_file = f"{report_name}.csv"

        with open(
                csv_file,
                "w",
                newline="",
                encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            for row in rows:

                values = [
                    c.get(
                        "VarCharValue",
                        ""
                    )
                    for c in row["Data"]
                ]

                writer.writerow(values)

        row_count = len(rows) - 1

        print(
            f"Report '{report_name}' "
            f"complete: {row_count} rows "
            f"written to {csv_file}"
        )

        return row_count

    def save_to_s3(
            self,
            bucket,
            key,
            local_path):

        self.s3.upload_file(
            local_path,
            bucket,
            key
        )

        print(
            f"Uploaded to "
            f"s3://{bucket}/{key}"
        )