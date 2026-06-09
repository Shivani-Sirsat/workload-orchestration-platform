import json
from pathlib import Path


RESULTS_DIR = Path("results")


def save_result(
    workload_name,
    result
):

    RESULTS_DIR.mkdir(
        exist_ok=True
    )

    file_path = (
        RESULTS_DIR /
        f"{workload_name}.json"
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