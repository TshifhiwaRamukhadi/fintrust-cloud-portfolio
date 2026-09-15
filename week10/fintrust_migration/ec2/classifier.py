from ..utils.sessions import get_client

VALID_STRATEGIES = {
    "rehost",
    "replatform",
    "refactor",
    "retire",
    "retain",
    "repurchase"
}


def _get_tag(tags, key):

    for tag in (tags or []):

        if tag["Key"] == key:
            return tag["Value"]

    return None


def classify_instances(tag_prefix="migration"):

    ec2 = get_client("ec2")

    paginator = ec2.get_paginator(
        "describe_instances"
    )

    portfolio = {
        strategy: []
        for strategy in VALID_STRATEGIES
    }

    untagged = []

    for page in paginator.paginate():

        for reservation in page["Reservations"]:

            for instance in reservation["Instances"]:

                tags = instance.get("Tags", [])

                strategy = _get_tag(
                    tags,
                    f"{tag_prefix}:strategy"
                )

                name = (
                    _get_tag(tags, "Name")
                    or instance["InstanceId"]
                )

                wave = (
                    _get_tag(
                        tags,
                        f"{tag_prefix}:wave"
                    )
                    or "unassigned"
                )

                entry = {
                    "id": instance["InstanceId"],
                    "name": name,
                    "type": instance["InstanceType"],
                    "state": instance["State"]["Name"],
                    "wave": wave,
                    "strategy": strategy
                }

                if strategy in VALID_STRATEGIES:

                    portfolio[strategy].append(
                        entry
                    )

                else:

                    untagged.append(
                        entry
                    )

    return portfolio, untagged


def get_migration_wave(wave_number):

    portfolio, _ = classify_instances()

    return [
        instance
        for instances in portfolio.values()
        for instance in instances
        if instance["wave"] == str(wave_number)
    ]
