import json
import boto3
from datetime import datetime, timedelta

BUCKET_NAME = "fintrust-transactions-prod"

s3 = boto3.client("s3")

TOP_CUSTOMERS = [

    {
        "customer_id": "C1001",
        "risk_score": 0.92,
        "spike_flag": 1
    },

    {
        "customer_id": "C1002",
        "risk_score": 0.89,
        "spike_flag": 1
    },

    {
        "customer_id": "C1003",
        "risk_score": 0.81,
        "spike_flag": 0
    }

]


def has_recent_s3_activity(
    customer_id
):

    seven_days_ago = (
        datetime.utcnow()
        -
        timedelta(days=7)
    )

    try:

        response = s3.list_objects_v2(
            Bucket=BUCKET_NAME,
            Prefix=f"{customer_id}/"
        )

        for obj in response.get(
            "Contents",
            []
        ):

            if (
                obj["LastModified"]
                .replace(
                    tzinfo=None
                )
                >= seven_days_ago
            ):
                return True

    except Exception:

        return False

    return False


def build_report():

    findings = []

    for customer in TOP_CUSTOMERS:

        findings.append({

            "customer_id":
                customer["customer_id"],

            "risk_score":
                customer["risk_score"],

            "spike_flag":
                customer["spike_flag"],

            "s3_activity_7d":
                has_recent_s3_activity(
                    customer[
                        "customer_id"
                    ]
                )

        })

    return findings


if __name__ == "__main__":

    report = {

        "report_date":
            datetime.utcnow()
            .isoformat(),

        "high_risk_customers":
            build_report()

    }

    print(
        json.dumps(
            report,
            indent=2,
            default=str
        )
    )