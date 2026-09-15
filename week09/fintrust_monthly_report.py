import boto3
from datetime import datetime
from cost_explorer_report import (
    get_monthly_spend_by_service
)

s3 = boto3.client("s3")

BUCKET = "fintrust-cost-reports"


class FinTrustMonthlyReport:

    def build_report(
            self,
            year,
            months):

        monthly_data = []

        for month in months:

            monthly_data.append(
                get_monthly_spend_by_service(
                    year,
                    month
                )
            )

        services = {}

        for report in monthly_data:

            for service, cost in report.items():

                services.setdefault(
                    service,
                    []
                ).append(cost)

        averages = {
            service:
            sum(costs) / len(costs)
            for service, costs
            in services.items()
        }

        top5 = sorted(
            averages.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        lines = []

        lines.append(
            "FINTRUST MONTHLY COST REPORT"
        )

        lines.append(
            "=" * 70
        )

        for service, _ in top5:

            month1 = (
                monthly_data[0]
                .get(service, 0)
            )

            month2 = (
                monthly_data[1]
                .get(service, 0)
            )

            month3 = (
                monthly_data[2]
                .get(service, 0)
            )

            change = (
                ((month3 - month2)
                / month2) * 100
            ) if month2 else 0

            sign = (
                "+"
                if change >= 0
                else ""
            )

            lines.append(
                f"{service:<35}"
                f"{month1:>10.2f}"
                f"{month2:>10.2f}"
                f"{month3:>10.2f}"
                f"{sign}{change:>7.1f}%"
            )

        return "\n".join(lines)

    def upload_report(
            self,
            report_text):

        now = datetime.utcnow()

        key = (
            f"{now.year}-"
            f"{now.month:02d}/"
            f"monthly_summary.txt"
        )

        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=report_text.encode(
                "utf-8"
            )
        )

        print(
            f"Uploaded to "
            f"s3://{BUCKET}/{key}"
        )