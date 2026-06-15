from database.repository import (
    save_run,
    save_metric
)

run_id = save_run(
    "20260615_140000",
    "redis-benchmark",
    "docker",
    "local"
)

save_metric(
    run_id,
    "get_rps",
    100000
)

save_metric(
    run_id,
    "set_rps",
    90000
)

print(
    f"Inserted run {run_id}"
)