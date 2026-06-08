import subprocess

from cli.workload_registry import get_workload


def deploy(workload_name):

    workload = get_workload(workload_name)

    if workload["stack"] == "redis-stack":

        print(
            f"Deploying {workload_name} to Docker..."
        )

        container_name = "redis-benchmark-container"

        subprocess.run(
            [
                "docker",
                "rm",
                "-f",
                container_name
            ],
            capture_output=True
        )

        result = subprocess.run(
            [
                "docker",
                "run",
                "-d",
                "--name",
                container_name,
                "-p",
                "6379:6379",
                "redis:7"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:

            print(result.stderr)

            return False

        print(
            f"Container started: {container_name}"
        )

        return True

    print(
        f"No Docker deployment implemented for stack: "
        f"{workload['stack']}"
    )

    return False