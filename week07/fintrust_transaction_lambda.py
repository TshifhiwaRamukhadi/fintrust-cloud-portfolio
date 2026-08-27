import json
import os
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs = boto3.client("sqs")

QUEUE_URL = os.environ.get(
    "PAYMENT_QUEUE_URL",
    ""
)


def lambda_handler(event, context):

    body_str = (
        event.get("body")
        or "{}"
    )

    body = json.loads(
        body_str
    )

    account_id = body.get(
        "account_id"
    )

    amount = body.get(
        "amount"
    )

    if not account_id or not amount:

        return {
            "statusCode": 400,
            "body": json.dumps({
                "error":
                "account_id and amount required"
            })
        }

    logger.info(
        "Processing transaction "
        "for account %s amount %s",
        account_id,
        amount
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "accepted",
            "account_id": account_id
        })
    }