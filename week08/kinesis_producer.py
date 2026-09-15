import boto3
import json
import uuid
import datetime

kinesis = boto3.client(
    "kinesis",
    region_name="af-south-1"
)

STREAM_NAME = "transaction-stream"


def publish_transaction(
        account_id,
        amount,
        currency,
        tx_type):

    event = {
        "transaction_id":
            str(uuid.uuid4()),
        "account_id":
            account_id,
        "amount":
            amount,
        "currency":
            currency,
        "type":
            tx_type,
        "timestamp":
            datetime.datetime.utcnow()
            .isoformat()
    }

    response = kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(event).encode(
            "utf-8"
        ),
        PartitionKey=account_id
    )

    return (
        response["SequenceNumber"],
        response["ShardId"]
    )


if __name__ == "__main__":

    for i in range(5):

        seq, shard = publish_transaction(
            account_id=
                f"ACC-{i % 3:04d}",
            amount=
                round(
                    1000 * (i + 1),
                    2
                ),
            currency="ZAR",
            tx_type="PAYMENT"
        )

        print(
            f"Published to {shard}, "
            f"sequence: "
            f"{seq[:20]}..."
        )