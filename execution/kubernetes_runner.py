import subprocess
import re

from execution.result_writer import (
    save_result
)

from execution.log_writer import (
    save_log
)


def run(workload_name):

    if workload_name == "tpcc-postgresql":

        print(
            "Executing PostgreSQL benchmark..."
        )

        result = subprocess.run(
            [
                "kubectl",
                "exec",
                "-i",
                "tpcc-postgresql-7d8bb9cdcb-gjdpz",
                "--",
                "pgbench",
                "-U",
                "postgres",
                "-c",
                "10",
                "-t",
                "100",
                "pgbench"
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

        tps_match = re.search(
            r"tps = ([\d\.]+)",
            result.stdout
        )

        latency_match = re.search(
            r"latency average = ([\d\.]+)",
            result.stdout
        )

        kpis = {
            "tps": float(
                tps_match.group(1)
            ),
            "latency_ms": float(
                latency_match.group(1)
            )
        }

        save_result(
            workload_name,
            "kubernetes",
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