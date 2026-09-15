import boto3
from datetime import datetime

dms = boto3.client(
    "database-migration-service",
    region_name="eu-north-1"
)

def get_task_progress(task_arn):

    response = dms.describe_replication_tasks(
        Filters=[
            {
                "Name": "replication-task-arn",
                "Values": [task_arn]
            }
        ]
    )

    if not response["ReplicationTasks"]:
        return None

    task = response["ReplicationTasks"][0]

    return {
        "task_id":
            task["ReplicationTaskIdentifier"],
        "status":
            task["Status"]
    }

print(
    "DMS monitor ready."
)