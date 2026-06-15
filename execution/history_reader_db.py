from database.repository import (
    get_runs,
    get_metrics
)


def load_history(
    workload_name
):

    runs = get_runs(
        workload_name
    )

    history = []

    for run in runs:

        run_id = run[0]

        metrics = get_metrics(
            run_id
        )

        history.append(
            {
                "run": run[1],
                "kpis": {
                    metric[0]: metric[1]
                    for metric in metrics
                }
            }
        )

    return history