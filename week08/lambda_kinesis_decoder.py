import base64
import json


def lambda_handler(
        event,
        context):

    for record in event["Records"]:

        raw = base64.b64decode(
            record["kinesis"]["data"]
        )

        transaction = json.loads(
            raw.decode("utf-8")
        )

        print(
            f"Received: "
            f"{transaction['transaction_id']} | "
            f"Account: "
            f"{transaction['account_id']} | "
            f"Amount: "
            f"{transaction['amount']} "
            f"{transaction['currency']}"
        )


simulated_event = {

    "Records": [

        {
            "kinesis": {

                "data":
                base64.b64encode(

                    json.dumps({

                        "transaction_id":
                            "txn-test-001",

                        "account_id":
                            "ACC-0001",

                        "amount":
                            15000.00,

                        "currency":
                            "ZAR",

                        "type":
                            "PAYMENT"

                    }).encode()

                ).decode()
            }
        }
    ]
}

if __name__ == "__main__":
    lambda_handler(
        simulated_event,
        None
    )