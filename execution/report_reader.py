import json

from pathlib import Path


RESULTS_DIR = Path("results")


def generate_report(
    workload_name
):

    workload_dir = (
        RESULTS_DIR /
        workload_name
    )

    if not workload_dir.exists():

        return None

    files = sorted(
        workload_dir.glob("*.json")
    )

    if not files:

        return None

    runs = []

    for file_path in files:

        with open(
            file_path,
            "r"
        ) as file:

            runs.append(
                json.load(file)
            )

    return runs