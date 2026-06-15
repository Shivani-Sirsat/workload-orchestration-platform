import json

from pathlib import Path
from datetime import datetime

from database.repository import (
    save_run,
    save_metric
)


RESULTS_DIR = Path("results")


def save_result(
    workload_name,
    target,
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

    metadata = {
        "timestamp": timestamp,
        "workload": workload_name,
        "target": target,
        "host": "local"
    }

    metadata.update(
        result
    )

    #
    # Save JSON (existing behavior)
    #

    with open(
        file_path,
        "w"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=4
        )

    #
    # Save PostgreSQL
    #

    run_id = save_run(
        timestamp,
        workload_name,
        target,
        "local"
    )

    for key, value in result.items():

        if isinstance(
            value,
            (int, float)
        ):

            save_metric(
                run_id,
                key,
                value
            )

    return file_path