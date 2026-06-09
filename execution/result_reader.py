import json
from pathlib import Path


RESULTS_DIR = Path("results")


def load_result(
    workload_name
):

    file_path = (
        RESULTS_DIR /
        f"{workload_name}.json"
    )

    if not file_path.exists():

        return None

    with open(
        file_path,
        "r"
    ) as file:

        return json.load(file)