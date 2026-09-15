import math

DEVICE_SPECS = {
    "Snowcone-HDD": {
        "usable_tb": 8,
        "description": "Smallest edge device"
    },
    "Snowcone-SSD": {
        "usable_tb": 14,
        "description": "SSD enabled Snowcone"
    },
    "Snowball-Edge-Storage-Opt": {
        "usable_tb": 80,
        "description": "High-capacity storage migration"
    },
    "Snowball-Edge-Compute-Opt": {
        "usable_tb": 28,
        "description": "Edge compute workloads"
    },
    "Snowmobile": {
        "usable_tb": 100000,
        "description": "Exabyte-scale migration"
    }
}

SNOWMOBILE_THRESHOLD_TB = 10000


def plan_snow_transfer(
    data_size_tb,
    purpose="archive"
):

    if data_size_tb >= SNOWMOBILE_THRESHOLD_TB:

        device = "Snowmobile"

        count = math.ceil(
            data_size_tb /
            DEVICE_SPECS[device]["usable_tb"]
        )

        return {
            "device": device,
            "count": count,
            "total_capacity_tb":
                count *
                DEVICE_SPECS[device]["usable_tb"]
        }

    device = (
        "Snowball-Edge-Storage-Opt"
        if purpose == "archive"
        else "Snowball-Edge-Compute-Opt"
    )

    usable = DEVICE_SPECS[device]["usable_tb"]

    count = math.ceil(
        data_size_tb / usable
    )

    return {
        "device": device,
        "count": count,
        "total_capacity_tb":
            count * usable,
        "overhead_tb":
            round(
                count * usable -
                data_size_tb,
                1
            ),
        "description":
            DEVICE_SPECS[device]["description"]
    }


if __name__ == "__main__":

    plan = plan_snow_transfer(
        3000,
        purpose="archive"
    )

    print(f"Device: {plan['device']}")
    print(f"Count: {plan['count']} devices")
    print(
        f"Total Capacity: "
        f"{plan['total_capacity_tb']} TB"
    )
    print(
        f"Overhead: "
        f"{plan['overhead_tb']} TB"
    )

    gbps = 1.0

    transfer_days = (
        (3000 * 1024)
        /
        (
            gbps *
            3600 *
            24 /
            8
        )
    )

    print(
        f"\nInternet Transfer "
        f"(1 Gbps): "
        f"{transfer_days:.0f} days"
    )

    print(
        "Snow Transfer: "
        "~2-3 weeks"
    )