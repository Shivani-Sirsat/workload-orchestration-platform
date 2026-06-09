import json

from pathlib import Path


RESULTS_DIR = Path("results")


def load_history(
    workload_name
):

    workload_dir = (
        RESULTS_DIR /
        workload_name
    )

    if not workload_dir.exists():

        return []

    history = []

    for file_path in sorted(
        workload_dir.glob("*.json")
    ):

        with open(
            file_path,
            "r"
        ) as file:

            data = json.load(file)

        history.append(
            {
                "run": file_path.stem,
                "kpis": data
            }
        )

    return history