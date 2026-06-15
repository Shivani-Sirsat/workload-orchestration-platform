from execution.history_reader_db import (
    load_history
)

history = load_history(
    "redis-benchmark"
)

for run in history:

    print(
        f"Run: {run['run']}"
    )

    for key, value in run["kpis"].items():

        print(
            f"  {key}: {value}"
        )

    print()