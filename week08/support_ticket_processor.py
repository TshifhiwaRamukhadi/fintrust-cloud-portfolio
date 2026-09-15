import boto3
import json

from comprehend_pii_redaction import (
    redact_pii
)

comp = boto3.client(
    "comprehend",
    region_name="af-south-1"
)

sqs = boto3.client(
    "sqs",
    region_name="af-south-1"
)

URGENT_QUEUE_URL = (
    "https://sqs.af-south-1.amazonaws.com/"
    "ACCOUNT_ID/"
    "fintrust-support-urgent"
)

STANDARD_QUEUE_URL = (
    "https://sqs.af-south-1.amazonaws.com/"
    "ACCOUNT_ID/"
    "fintrust-support-standard"
)


def process_support_ticket(
        ticket_text):

    redacted_text, pii_types = (
        redact_pii(ticket_text)
    )

    sentiment_response = (
        comp.detect_sentiment(
            Text=ticket_text,
            LanguageCode="en"
        )
    )

    sentiment = (
        sentiment_response[
            "Sentiment"
        ]
    )

    queue_url = (
        URGENT_QUEUE_URL
        if sentiment == "NEGATIVE"
        else STANDARD_QUEUE_URL
    )

    message = {
        "redacted_text":
            redacted_text,

        "sentiment":
            sentiment,

        "pii_types_found":
            pii_types,

        "priority":
            "HIGH"
            if sentiment == "NEGATIVE"
            else "STANDARD"
    }

    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(
            message
        )
    )

    return message