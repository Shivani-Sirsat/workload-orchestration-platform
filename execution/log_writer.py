from pathlib import Path
from datetime import datetime


LOGS_DIR = Path("logs")


def save_log(
    workload_name,
    output
):

    workload_dir = (
        LOGS_DIR /
        workload_name
    )

    workload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = (
        workload_dir /
        f"{timestamp}.log"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(output)

    return file_path