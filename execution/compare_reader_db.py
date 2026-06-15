from database.repository import (
    get_recent_runs,
    get_metrics
)


def load_compare_data(
    workload_name
):

    runs = get_recent_runs(
        workload_name
    )

    if len(runs) < 2:

        return None, None

    latest_run = runs[0]
    previous_run = runs[1]

    latest_metrics = dict(
        get_metrics(
            latest_run[0]
        )
    )

    previous_metrics = dict(
        get_metrics(
            previous_run[0]
        )
    )

    return (
        previous_metrics,
        latest_metrics
    )