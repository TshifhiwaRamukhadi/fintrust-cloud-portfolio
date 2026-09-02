import json
import boto3

from datetime import datetime
from datetime import timezone

iam = boto3.client("iam")


def get_users_without_mfa():

    violations = []

    paginator = iam.get_paginator(
        "list_users"
    )

    for page in paginator.paginate():

        for user in page["Users"]:

            username = user["UserName"]

            try:
                iam.get_login_profile(
                    UserName=username
                )

            except iam.exceptions.NoSuchEntityException:
                continue

            mfa_response = (
                iam.list_mfa_devices(
                    UserName=username
                )
            )

            if not mfa_response["MFADevices"]:

                violations.append({
                    "username": username,
                    "created":
                        user[
                            "CreateDate"
                        ].isoformat()
                })

    return violations


def get_stale_access_keys():

    findings = []

    paginator = iam.get_paginator(
        "list_users"
    )

    for page in paginator.paginate():

        for user in page["Users"]:

            username = user["UserName"]

            access_keys = (
                iam.list_access_keys(
                    UserName=username
                )
            )

            for key in access_keys[
                "AccessKeyMetadata"
            ]:

                key_age = (
                    datetime.now(
                        timezone.utc
                    )
                    -
                    key["CreateDate"]
                ).days

                if key_age > 90:

                    findings.append({
                        "username":
                            username,
                        "access_key":
                            key[
                                "AccessKeyId"
                            ],
                        "age_days":
                            key_age
                    })

    return findings


def save_report_to_s3(
    bucket,
    findings
):

    s3 = boto3.client("s3")

    today = datetime.utcnow().strftime(
        "%Y/%m/%d"
    )

    key = (
        f"security-audit/"
        f"{today}/"
        f"findings.json"
    )

    report = {
        "report_date":
            datetime.utcnow().isoformat(),
        "findings":
            findings
    }

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(
            report,
            indent=2,
            default=str
        ),
        ContentType="application/json",
        ServerSideEncryption="aws:kms"
    )

    print(
        f"Report saved to "
        f"s3://{bucket}/{key}"
    )


if __name__ == "__main__":

    findings = {
        "iam_mfa_violations":
            get_users_without_mfa(),

        "iam_stale_access_keys":
            get_stale_access_keys()
    }

    print(
        json.dumps(
            findings,
            indent=2,
            default=str
        )
    )

    # Uncomment when AWS credentials exist
    # save_report_to_s3(
    #     "fintrust-audit-reports",
    #     findings
    # )