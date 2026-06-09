import subprocess

from execution.kpi_parser import (
    parse_redis_kpi
)

from execution.result_writer import (
    save_result
)

from execution.log_writer import (
    save_log
)


def run(workload_name):

    if workload_name == "redis-benchmark":

        print(
            "Executing Redis benchmark..."
        )

        result = subprocess.run(
            [
                "docker",
                "exec",
                "redis-benchmark-container",
                "redis-benchmark",
                "-q"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:

            return {
                "status": "failed",
                "message": result.stderr
            }

        save_log(
            workload_name,
            result.stdout
        )

        kpis = parse_redis_kpi(
            result.stdout
        )

        save_result(
            workload_name,
            kpis
        )

        return {
            "status": "success",
            "output": kpis
        }

    return {
        "status": "failed",
        "message": f"No runner implemented for {workload_name}"
    }