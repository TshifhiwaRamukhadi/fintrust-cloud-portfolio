import boto3
import pathlib

s3 = boto3.client(
    "s3",
    region_name="af-south-1"
)

BUCKET = "fintrust-processed"


def upload_parquet_partition(
        local_path,
        s3_key):

    s3.upload_file(
        local_path,
        BUCKET,
        s3_key
    )

    print(
        f"Uploaded "
        f"s3://{BUCKET}/{s3_key}"
    )


for file in pathlib.Path(".").glob(
        "fintrust_processed/**/*.parquet"):

    s3_key = (
        "transactions/"
        +
        str(file)
        .replace(
            "fintrust_processed\\",
            ""
        )
        .replace("\\", "/")
    )

    upload_parquet_partition(
        str(file),
        s3_key
    )