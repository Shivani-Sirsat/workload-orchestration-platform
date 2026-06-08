import subprocess

from cli.workload_registry import get_workload


def deploy(workload_name):

    workload = get_workload(workload_name)

    print(
        f"Deploying {workload_name} to Kubernetes..."
    )

    if workload["stack"] == "postgres-stack":

        yaml_file = "k8s/postgres-deployment.yaml"

    else:

        print(
            f"No Kubernetes deployment implemented for stack: "
            f"{workload['stack']}"
        )

        return False

    result = subprocess.run(
        [
            "kubectl",
            "apply",
            "-f",
            yaml_file
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print(result.stderr)

        return False

    print(result.stdout)

    return True