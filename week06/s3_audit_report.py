import boto3


def is_public_access_blocked(s3_client, bucket_name):
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


def is_encrypted(s3_client, bucket_name):
    try:
        s3_client.get_bucket_encryption(
            Bucket=bucket_name
        )
        return True

    except Exception:
        return False


def main():
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    print(
        f"{'Bucket Name':40}"
        f"{'Region':15}"
        f"{'Access':12}"
        f"{'Encryption':12}"
    )

    print("-" * 80)

    for bucket in response["Buckets"]:
        name = bucket["Name"]

        try:
            location = s3.get_bucket_location(
                Bucket=name
            )

            region = (
                location["LocationConstraint"]
                or "us-east-1"
            )

        except Exception:
            region = "Unknown"

        access_status = (
            "SAFE"
            if is_public_access_blocked(s3, name)
            else "EXPOSED"
        )

        encryption_status = (
            "ENCRYPTED"
            if is_encrypted(s3, name)
            else "UNENCRYPTED"
        )

        print(
            f"{name:40}"
            f"{region:15}"
            f"{access_status:12}"
            f"{encryption_status:12}"
        )


if __name__ == "__main__":
    main()