import boto3

ec2 = boto3.client(
    "ec2",
    region_name="af-south-1"
)

RESTRICTED_PORTS = {
    22,
    3389,
    5432,
    3306,
    1521
}

OPEN_CIDR = "0.0.0.0/0"


def check_sg_exposure(sg):
    findings = []

    sg_id = sg["GroupId"]
    sg_name = sg.get(
        "GroupName",
        sg_id
    )

    for rule in sg.get(
        "IpPermissions",
        []
    ):

        from_port = rule.get(
            "FromPort",
            0
        )

        to_port = rule.get(
            "ToPort",
            65535
        )

        for ip_range in rule.get(
            "IpRanges",
            []
        ):

            if (
                ip_range["CidrIp"]
                == OPEN_CIDR
            ):

                exposed_ports = [
                    port
                    for port in RESTRICTED_PORTS
                    if from_port <= port <= to_port
                ]

                if (
                    exposed_ports or
                    (
                        from_port == 0
                        and to_port == 65535
                    )
                ):

                    findings.append({
                        "sg_id": sg_id,
                        "sg_name": sg_name,
                        "port_range":
                            f"{from_port}-{to_port}",
                        "cidr":
                            OPEN_CIDR,
                        "severity":
                            "CRITICAL"
                            if from_port == 0
                            else "HIGH"
                    })

    return findings


if __name__ == "__main__":

    paginator = ec2.get_paginator(
        "describe_security_groups"
    )

    findings = []

    for page in paginator.paginate():

        for sg in page[
            "SecurityGroups"
        ]:

            findings.extend(
                check_sg_exposure(sg)
            )

    print(
        f"Findings: {len(findings)}"
    )