import boto3

iam = boto3.client("iam")


def get_users_without_mfa():
    """
    Return IAM users with console access but no MFA.
    """
    violations = []

    paginator = iam.get_paginator("list_users")

    for page in paginator.paginate():
        for user in page["Users"]:
            username = user["UserName"]

            try:
                iam.get_login_profile(
                    UserName=username
                )
                has_console_access = True

            except iam.exceptions.NoSuchEntityException:
                has_console_access = False

            if not has_console_access:
                continue

            mfa_response = iam.list_mfa_devices(
                UserName=username
            )

            has_mfa = (
                len(mfa_response["MFADevices"]) > 0
            )

            if not has_mfa:
                violations.append({
                    "username": username,
                    "created":
                        user["CreateDate"].isoformat()
                })

    return violations


if __name__ == "__main__":
    violations = get_users_without_mfa()

    print(
        f"Users without MFA: "
        f"{len(violations)}"
    )

    for user in violations:
        print(
            f"- {user['username']}"
        )