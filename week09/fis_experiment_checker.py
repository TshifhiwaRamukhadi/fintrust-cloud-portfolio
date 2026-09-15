import boto3

fis = boto3.client(
    "fis",
    region_name="eu-north-1"
)

experiments = (
    fis.list_experiments()
    .get("experiments", [])
)

print(
    f"Experiments: {len(experiments)}"
)