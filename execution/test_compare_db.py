from execution.compare_reader_db import (
    load_compare_data
)

previous, latest = (
    load_compare_data(
        "redis-benchmark"
    )
)

print(
    "\nLatest Run\n"
)

print(
    latest
)

print(
    "\nPrevious Run\n"
)

print(
    previous
)