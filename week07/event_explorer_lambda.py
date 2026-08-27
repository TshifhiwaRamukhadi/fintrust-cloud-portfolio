import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ENVIRONMENT = os.environ.get(
    "ENVIRONMENT",
    "dev"
)


def lambda_handler(event, context):

    logger.info(
        "Event: %s",
        json.dumps(event)
    )

    logger.info(
        "Function name: %s",
        context.function_name
    )

    logger.info(
        "Remaining time: %s",
        context.get_remaining_time_in_millis()
    )

    logger.info(
        "Environment: %s",
        ENVIRONMENT
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ok"
        })
    }