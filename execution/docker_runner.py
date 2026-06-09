import subprocess


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

        return {
            "status": "success",
            "output": result.stdout
        }

    return {
        "status": "failed",
        "message": f"No runner implemented for {workload_name}"
    }