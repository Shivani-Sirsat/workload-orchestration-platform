from pathlib import Path


LOGS_DIR = Path("logs")


def save_log(
    workload_name,
    output
):

    LOGS_DIR.mkdir(
        exist_ok=True
    )

    file_path = (
        LOGS_DIR /
        f"{workload_name}.log"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(output)

    return file_path