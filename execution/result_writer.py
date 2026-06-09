import json

from pathlib import Path
from datetime import datetime


RESULTS_DIR = Path("results")


def save_result(
    workload_name,
    result
):

    workload_dir = (
        RESULTS_DIR /
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
        f"{timestamp}.json"
    )

    with open(
        file_path,
        "w"
    ) as file:

        json.dump(
            result,
            file,
            indent=4
        )

    return file_path