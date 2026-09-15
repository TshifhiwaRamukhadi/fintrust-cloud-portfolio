import boto3
from collections import defaultdict

tagging = boto3.client(
    "resourcegroupstaggingapi",
    region_name="af-south-1"
)

REQUIRED_TAGS = [
    "CostCentre",
    "Team",
    "Environment"
]


def audit_tag_compliance():

    non_compliant = {}

    total_resources = 0

    paginator = tagging.get_paginator(
        "get_resources"
    )

    for page in paginator.paginate():

        for resource in page[
            "ResourceTagMappingList"
        ]:

            total_resources += 1

            arn = resource["ResourceARN"]

            existing_keys = {
                tag["Key"]
                for tag in resource.get(
                    "Tags", []
                )
            }

            missing = [

                tag

                for tag in REQUIRED_TAGS

                if tag not in existing_keys

            ]

            if missing:
                non_compliant[arn] = missing

    return (
        total_resources,
        non_compliant
    )


if __name__ == "__main__":

    total, violations = (
        audit_tag_compliance()
    )

    print(
        f"Resources scanned: {total}"
    )

    print(
        f"Violations: "
        f"{len(violations)}"
    )

    by_service = defaultdict(int)

    for arn in violations:

        service = arn.split(":")[2]

        by_service[
            service
        ] += 1

    for service, count in sorted(
            by_service.items()):

        print(
            f"{service}: {count}"
        )