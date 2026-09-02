import boto3

glue = boto3.client(
    "glue",
    region_name="af-south-1"
)

# List databases

db_response = glue.get_databases()

for db in db_response["DatabaseList"]:

    print(
        f"Database: {db['Name']}"
    )

# List tables

tbl_response = glue.get_tables(
    DatabaseName="fintrust_curated"
)

for tbl in tbl_response["TableList"]:

    print(
        f"Table: {tbl['Name']}"
    )

# Table schema

tbl_detail = glue.get_table(
    DatabaseName="fintrust_curated",
    Name="transactions"
)

columns = (
    tbl_detail["Table"]
              ["StorageDescriptor"]
              ["Columns"]
)

print("\nSchema")

for col in columns:

    print(
        f"{col['Name']} "
        f"{col['Type']}"
    )

partition_keys = (
    tbl_detail["Table"]
              ["PartitionKeys"]
)

print("\nPartitions")

for pk in partition_keys:

    print(
        f"{pk['Name']} "
        f"{pk['Type']}"
    )