import json

from pathlib import Path


RESULTS_DIR = Path("results")


def load_latest_two_runs(
    workload_name
):

    workload_dir = (
        RESULTS_DIR /
        workload_name
    )

    if not workload_dir.exists():

        return None, None

    files = sorted(
        workload_dir.glob("*.json")
    )

    if len(files) < 2:

        return None, None

    previous_file = files[-2]
    latest_file = files[-1]

    with open(previous_file, "r") as file:

        previous = json.load(file)

    with open(latest_file, "r") as file:

        latest = json.load(file)

    return previous, latest