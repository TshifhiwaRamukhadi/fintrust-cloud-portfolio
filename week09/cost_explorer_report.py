import boto3

ce = boto3.client(
    "ce",
    region_name="us-east-1"
)


def get_monthly_spend_by_service(year, month):
    """
    Returns service spend for a month.
    """

    start = f"{year}-{month:02d}-01"

    if month == 12:
        end = f"{year + 1}-01-01"
    else:
        end = f"{year}-{month + 1:02d}-01"

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    results = {}

    for group in response["ResultsByTime"][0]["Groups"]:

        service = group["Keys"][0]

        cost = float(
            group["Metrics"]
            ["UnblendedCost"]
            ["Amount"]
        )

        if cost > 0.01:
            results[service] = round(cost, 2)

    return dict(
        sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )


if __name__ == "__main__":

    spend = get_monthly_spend_by_service(
        2024,
        6
    )

    total = sum(spend.values())

    print("\nTop Services\n")

    for service, cost in list(spend.items())[:10]:

        pct = (
            cost / total * 100
        ) if total else 0

        print(
            f"{service:<40}"
            f"${cost:>10,.2f} "
            f"({pct:.1f}%)"
        )

    print(
        f"\nTotal Spend: "
        f"${total:,.2f}"
    )