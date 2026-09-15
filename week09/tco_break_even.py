def tco_break_even(
        on_prem_annual_cost,
        aws_monthly_cost,
        migration_one_time_cost,
        onprem_inflation_pct=0.03):

    break_even = None

    print(
        "\nYear Comparison"
    )

    for year in range(1, 6):

        annual_onprem = (
            on_prem_annual_cost *
            ((1 + onprem_inflation_pct)
             ** (year - 1))
        )

        cumulative_onprem = sum(
            on_prem_annual_cost *
            ((1 + onprem_inflation_pct)
             ** i)
            for i in range(year)
        )

        cumulative_aws = (
            migration_one_time_cost +
            (aws_monthly_cost *
             year * 12)
        )

        difference = (
            cumulative_onprem -
            cumulative_aws
        )

        print(
            f"Year {year}: "
            f"OnPrem=${cumulative_onprem:,.0f} "
            f"AWS=${cumulative_aws:,.0f} "
            f"Diff=${difference:,.0f}"
        )

    for month in range(1, 61):

        years_elapsed = (
            month / 12
        )

        cumulative_onprem = 0

        for yr in range(
                int(years_elapsed)
                + 1):

            cumulative_onprem += (
                on_prem_annual_cost *
                ((1 + onprem_inflation_pct)
                 ** yr)
            ) / 12

        cumulative_onprem *= month

        cumulative_aws = (
            migration_one_time_cost +
            aws_monthly_cost *
            month
        )

        if (
            cumulative_aws <
            cumulative_onprem
        ):
            break_even = month
            break

    return break_even


if __name__ == "__main__":

    month = tco_break_even(
        on_prem_annual_cost=4200000,
        aws_monthly_cost=248000,
        migration_one_time_cost=850000,
        onprem_inflation_pct=0.03
    )

    print(
        f"\nBreak-even month: "
        f"{month}"
    )