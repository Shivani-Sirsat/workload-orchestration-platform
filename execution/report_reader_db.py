from database.repository import (
    get_runs,
    get_metrics
)


def generate_report(
    workload_name
):

    runs = get_runs(
        workload_name
    )

    report_data = []

    for run in runs:

        run_id = run[0]

        metrics = dict(
            get_metrics(
                run_id
            )
        )

        report = {
            "timestamp": run[1],
            "workload": run[2],
            "target": run[3],
            "host": run[4]
        }

        report.update(
            metrics
        )

        report_data.append(
            report
        )

    return report_data