import boto3
import json
from collections import defaultdict
from datetime import datetime

from tag_compliance_audit import (
    audit_tag_compliance
)

tagging = boto3.client(
    "resourcegroupstaggingapi",
    region_name="af-south-1"
)

s3 = boto3.client("s3")

BUCKET = "fintrust-governance"


def build_governance_report():

    total_scanned, violations = (
        audit_tag_compliance()
    )

    initial_violations = len(
        violations
    )

    auto_remediated = 0

    failed = 0

    by_service = defaultdict(int)

    for arn, missing_tags in (
            violations.items()):

        service = arn.split(":")[2]

        by_service[service] += 1

        try:

            tagging.tag_resources(
                ResourceARNList=[arn],
                Tags={
                    "Environment":
                    "Production"
                }
            )

            auto_remediated += 1

        except Exception:

            failed += 1

    _, remaining = (
        audit_tag_compliance()
    )

    report = {

        "report_date":
            datetime.utcnow()
            .strftime("%Y-%m-%d"),

        "total_scanned":
            total_scanned,

        "initial_violations":
            initial_violations,

        "auto_remediated":
            auto_remediated,

        "remediation_failures":
            failed,

        "remaining_violations":
            len(remaining),

        "violations_by_service":
            dict(by_service)
    }

    key = (
        datetime.utcnow()
        .strftime("%Y-%m-%d")
        + ".json"
    )

    s3.put_object(
        Bucket=BUCKET,
        Key=f"tag-audit/{key}",
        Body=json.dumps(
            report,
            indent=2
        ).encode("utf-8")
    )

    print(
        json.dumps(
            report,
            indent=2
        )
    )


if __name__ == "__main__":
    build_governance_report()