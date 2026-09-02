import boto3
import json

pricing = boto3.client(
    "pricing",
    region_name="us-east-1"
)


def get_ec2_ondemand_price(
        instance_type,
        region="af-south-1",
        os="Linux"):

    region_names = {
        "af-south-1":
            "Africa (Cape Town)",
        "eu-west-1":
            "Europe (Ireland)",
        "us-east-1":
            "US East (N. Virginia)"
    }

    response = pricing.get_products(
        ServiceCode="AmazonEC2",
        Filters=[
            {
                "Type": "TERM_MATCH",
                "Field": "instanceType",
                "Value": instance_type
            },
            {
                "Type": "TERM_MATCH",
                "Field": "location",
                "Value": region_names[region]
            },
            {
                "Type": "TERM_MATCH",
                "Field": "operatingSystem",
                "Value": os
            },
            {
                "Type": "TERM_MATCH",
                "Field": "tenancy",
                "Value": "Shared"
            },
            {
                "Type": "TERM_MATCH",
                "Field": "preInstalledSw",
                "Value": "NA"
            },
            {
                "Type": "TERM_MATCH",
                "Field": "capacityStatus",
                "Value": "Used"
            }
        ],
        MaxResults=1
    )

    if not response["PriceList"]:
        return None

    product = json.loads(
        response["PriceList"][0]
    )

    terms = product["terms"]["OnDemand"]

    price_dimensions = next(
        iter(
            next(
                iter(
                    terms.values()
                )
            )["priceDimensions"].values()
        )
    )

    return float(
        price_dimensions[
            "pricePerUnit"
        ]["USD"]
    )


if __name__ == "__main__":

    for inst in [
        "m5.xlarge",
        "r5.2xlarge",
        "c5.large"
    ]:

        price = get_ec2_ondemand_price(
            inst
        )

        if price:

            print(
                f"{inst}: "
                f"${price:.4f}/hr "
                f"= ${price*730:.2f}/month"
            )

        else:

            print(
                f"{inst}: "
                f"price not found"
            )