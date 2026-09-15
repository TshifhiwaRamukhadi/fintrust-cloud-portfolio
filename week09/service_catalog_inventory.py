import boto3

sc = boto3.client(
    "servicecatalog",
    region_name="af-south-1"
)


def list_portfolios_and_products():

    shared = (
        sc.list_accepted_portfolio_shares()
    )["PortfolioDetails"]

    owned = (
        sc.list_portfolios()
    )["PortfolioDetails"]

    portfolios = {
        p["Id"]: p
        for p in shared + owned
    }

    for pid, portfolio in portfolios.items():

        print(
            f"\nPortfolio: "
            f"{portfolio['DisplayName']}"
        )

        products = (
            sc.search_products_as_admin(
                PortfolioId=pid
            )
        )["ProductViewDetails"]

        for item in products:

            product = (
                item[
                    "ProductViewSummary"
                ]
            )

            print(
                f"  Product: "
                f"{product['Name']} | "
                f"Type: {product['Type']} | "
                f"Owner: {product['Owner']}"
            )


if __name__ == "__main__":
    list_portfolios_and_products()