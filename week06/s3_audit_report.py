import boto3
from botocore.exceptions import (
    NoCredentialsError,
    ClientError,
)


def is_public_access_blocked(s3_client, bucket_name):
    """
    Returns True if all four Public Access Block
    settings are enabled.
    """

    try:
        response = s3_client.get_public_access_block(
            Bucket=bucket_name
        )

        config = response["PublicAccessBlockConfiguration"]

        return all([
            config.get("BlockPublicAcls", False),
            config.get("IgnorePublicAcls", False),
            config.get("BlockPublicPolicy", False),
            config.get("RestrictPublicBuckets", False),
        ])

    except s3_client.exceptions.NoSuchPublicAccessBlockConfiguration:
        return False

    except ClientError:
        return False


def is_encrypted(s3_client, bucket_name):
    """
    Returns True if bucket encryption exists.
    """

    try:
        s3_client.get_bucket_encryption(
            Bucket=bucket_name
        )
        return True

    except ClientError:
        return False


def get_bucket_region(s3_client, bucket_name):
    """
    Retrieves the AWS Region for a bucket.
    """

    try:
        location = s3_client.get_bucket_location(
            Bucket=bucket_name
        )

        return (
            location["LocationConstraint"]
            or "us-east-1"
        )

    except ClientError:
        return "Unknown"


def print_report_header(title):
    print(f"\n{title}")
    print("=" * 95)

    print(
        f"{'Bucket Name':40}"
        f"{'Region':18}"
        f"{'Access':15}"
        f"{'Encryption':15}"
    )

    print("-" * 95)


def main():
    try:
        s3 = boto3.client("s3")

        response = s3.list_buckets()

        print_report_header("S3 AUDIT REPORT")

        for bucket in response["Buckets"]:
            bucket_name = bucket["Name"]

            region = get_bucket_region(
                s3,
                bucket_name
            )

            access_status = (
                "SAFE"
                if is_public_access_blocked(
                    s3,
                    bucket_name
                )
                else "EXPOSED"
            )

            encryption_status = (
                "ENCRYPTED"
                if is_encrypted(
                    s3,
                    bucket_name
                )
                else "UNENCRYPTED"
            )

            print(
                f"{bucket_name:40}"
                f"{region:18}"
                f"{access_status:15}"
                f"{encryption_status:15}"
            )

        print("-" * 95)
        print("Audit completed successfully.")

    except NoCredentialsError:

        print("\nAWS credentials not found.")
        print("Running demo audit report instead...\n")

        demo_buckets = [
            {
                "name": "fintrust-portal-assets",
                "region": "af-south-1",
                "access": "SAFE",
                "encryption": "ENCRYPTED"
            },
            {
                "name": "fintrust-transactions-prod",
                "region": "af-south-1",
                "access": "SAFE",
                "encryption": "ENCRYPTED"
            },
            {
                "name": "fintrust-dev-bucket",
                "region": "us-east-1",
                "access": "EXPOSED",
                "encryption": "UNENCRYPTED"
            }
        ]

        print_report_header(
            "S3 AUDIT REPORT (DEMO MODE)"
        )

        for bucket in demo_buckets:
            print(
                f"{bucket['name']:40}"
                f"{bucket['region']:18}"
                f"{bucket['access']:15}"
                f"{bucket['encryption']:15}"
            )

        print("-" * 95)
        print("Demo audit completed successfully.")

    except ClientError as error:
        print(
            f"\nAWS API Error: "
            f"{error.response['Error']['Message']}"
        )

    except Exception as error:
        print(
            f"\nUnexpected Error: {error}"
        )


if __name__ == "__main__":
    main()