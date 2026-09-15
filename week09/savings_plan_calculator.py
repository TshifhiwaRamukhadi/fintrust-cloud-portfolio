def calculate_savings_plan_savings(
        hourly_commitment_usd,
        term_years=3,
        discount_pct=0.66):

    effective_ondemand_hourly = (
        hourly_commitment_usd /
        (1 - discount_pct)
    )

    hours = (
        term_years *
        365 *
        24
    )

    total_ondemand = (
        effective_ondemand_hourly *
        hours
    )

    total_sp = (
        hourly_commitment_usd *
        hours
    )

    savings = (
        total_ondemand -
        total_sp
    )

    return {
        "commitment_per_hour":
            hourly_commitment_usd,

        "effective_ondemand_hourly":
            round(
                effective_ondemand_hourly,
                4
            ),

        "total_ondemand_cost":
            round(
                total_ondemand,
                2
            ),

        "total_sp_cost":
            round(
                total_sp,
                2
            ),

        "total_savings_usd":
            round(
                savings,
                2
            ),

        "savings_pct":
            round(
                discount_pct * 100,
                1
            )
    }


if __name__ == "__main__":

    result = (
        calculate_savings_plan_savings(
            hourly_commitment_usd=32.47,
            term_years=3,
            discount_pct=0.66
        )
    )

    for k, v in result.items():

        print(
            f"{k}: {v}"
        )