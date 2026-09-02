import boto3
import json
import uuid
import datetime
import os

sqs = boto3.client(
    "sqs",
    region_name="af-south-1"
)

QUEUE_URL = os.environ.get(
    "PAYMENT_QUEUE_URL",
    ""
)


def send_transaction(transaction):

    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(transaction),
        MessageGroupId=transaction["account_id"],
        MessageDeduplicationId=transaction["id"]
    )

    return response


if __name__ == "__main__":

    txn = {
        "id": str(uuid.uuid4()),
        "account_id": "ACC-001",
        "amount": 5000,
        "currency": "ZAR",
        "status": "pending",
        "created_at":
            datetime.datetime.utcnow()
            .isoformat()
    }

    send_transaction(txn)