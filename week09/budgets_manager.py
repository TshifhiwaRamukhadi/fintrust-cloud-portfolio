import boto3

budgets = boto3.client(
    "budgets",
    region_name="us-east-1"
)

ACCOUNT_ID = (
    boto3.client("sts")
    .get_caller_identity()
    ["Account"]
)


def create_monthly_budget(
        budget_name,
        limit_usd,
        alert_pct,
        email):

    budgets.create_budget(
        AccountId=ACCOUNT_ID,
        Budget={
            "BudgetName": budget_name,
            "BudgetLimit": {
                "Amount": str(limit_usd),
                "Unit": "USD"
            },
            "TimeUnit": "MONTHLY",
            "BudgetType": "COST"
        },
        NotificationsWithSubscribers=[
            {
                "Notification": {
                    "NotificationType": "ACTUAL",
                    "ComparisonOperator":
                        "GREATER_THAN",
                    "Threshold":
                        alert_pct,
                    "ThresholdType":
                        "PERCENTAGE"
                },
                "Subscribers": [
                    {
                        "SubscriptionType":
                            "EMAIL",
                        "Address": email
                    }
                ]
            }
        ]
    )

    print(
        f"Created budget: "
        f"{budget_name}"
    )


def list_budgets():

    response = (
        budgets.describe_budgets(
            AccountId=ACCOUNT_ID
        )
    )

    for budget in response["Budgets"]:

        limit = float(
            budget["BudgetLimit"]
            ["Amount"]
        )

        actual = float(
            budget.get(
                "CalculatedSpend",
                {}
            ).get(
                "ActualSpend",
                {}
            ).get(
                "Amount",
                0
            )
        )

        pct = (
            actual / limit * 100
        ) if limit else 0

        print(
            f"{budget['BudgetName']}: "
            f"${actual:.2f}/"
            f"${limit:.2f} "
            f"({pct:.1f}%)"
        )
