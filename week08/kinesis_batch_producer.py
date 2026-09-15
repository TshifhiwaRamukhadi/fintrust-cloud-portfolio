import boto3
import json

kinesis = boto3.client(
    "kinesis",
    region_name="af-south-1"
)

STREAM_NAME = "transaction-stream"


def publish_batch(
        transactions):

    records = [

        {
            "Data":
                json.dumps(txn)
                .encode("utf-8"),

            "PartitionKey":
                txn["account_id"]
        }

        for txn in transactions
    ]

    response = kinesis.put_records(
        StreamName=STREAM_NAME,
        Records=records
    )

    failed = response[
        "FailedRecordCount"
    ]

    if failed > 0:

        print(
            f"Warning: "
            f"{failed} records failed"
        )

    return len(records) - failed