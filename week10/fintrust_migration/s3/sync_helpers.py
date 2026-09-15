from ..utils.sessions import get_client
import time
import os

MBPS_TO_BYTES = 1_000_000 / 8


def start_task_execution(task_arn):

    ds = get_client("datasync")

    response = ds.start_task_execution(
        TaskArn=task_arn
    )

    return response[
        "TaskExecutionArn"
    ]


def get_execution_status(execution_arn):

    ds = get_client("datasync")

    response = ds.describe_task_execution(
        TaskExecutionArn=execution_arn
    )

    return {
        "status":
            response["Status"],

        "files_prepared":
            response.get(
                "Result",
                {}
            ).get(
                "PrepareDuration"
            ),

        "files_transferred":
            response.get(
                "FilesTransferred",
                0
            ),

        "bytes_transferred":
            response.get(
                "BytesTransferred",
                0
            ),

        "files_verified":
            response.get(
                "FilesVerified",
                0
            ),

        "errors":
            response.get(
                "FilesDeleted",
                0
            ),

        "result":
            response.get(
                "Result",
                {}
            )
    }


def wait_for_execution(
    execution_arn,
    poll_seconds=60
):

    terminal = {
        "SUCCESS",
        "ERROR"
    }

    while True:

        info = get_execution_status(
            execution_arn
        )

        status = info["status"]

        transferred_gb = (
            info[
                "bytes_transferred"
            ] / 1024**3
        )

        print(
            f"{status} | "
            f"{info['files_transferred']} files | "
            f"{transferred_gb:.2f} GB"
        )

        if status in terminal:
            return info

        time.sleep(
            poll_seconds
        )


def set_task_throttle(
    task_arn,
    bandwidth_mbps
):

    ds = get_client(
        "datasync"
    )

    if bandwidth_mbps == 0:
        throttle = 0

    else:
        throttle = int(
            bandwidth_mbps *
            MBPS_TO_BYTES
        )

    ds.update_task(
        TaskArn=task_arn,
        Options={
            "BytesPerSecond":
                throttle
        }
    )

    label = (
        f"{bandwidth_mbps} Mbps"
        if throttle
        else "unlimited"
    )

    print(
        f"Task throttle updated "
        f"to {label}"
    )


def lambda_handler(
    event,
    context
):

    task_arn = os.getenv(
        "DATASYNC_TASK_ARN"
    )

    mode = event.get(
        "mode",
        "daytime"
    )

    throttle_map = {
        "daytime": 500,
        "overnight": 9000
    }

    bandwidth = throttle_map.get(
        mode,
        500
    )

    set_task_throttle(
        task_arn,
        bandwidth
    )

    return {
        "statusCode": 200,
        "mode": mode,
        "bandwidth_mbps":
            bandwidth
    }


def monitor_nightly_transfers(
    task_arns
):

    execution_arns = [
        start_task_execution(
            arn
        )
        for arn in task_arns
    ]

    terminal = {
        "SUCCESS",
        "ERROR"
    }

    results = {}

    while True:

        complete = True

        for execution_arn in execution_arns:

            info = get_execution_status(
                execution_arn
            )

            status = info["status"]

            gb = round(
                info[
                    "bytes_transferred"
                ] / 1024**3,
                2
            )

            print(
                f"{execution_arn[:20]} "
                f"| {status:10} "
                f"| {gb} GB"
            )

            if status not in terminal:
                complete = False

            results[
                execution_arn
            ] = info

        if complete:
            return results

        time.sleep(60)