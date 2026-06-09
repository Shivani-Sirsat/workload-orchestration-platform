from cli.workload_registry import get_workload

from execution.docker_runner import (
    run as docker_run
)

from execution.kubernetes_runner import (
    run as kubernetes_run
)


def execute_workload(
    workload_name,
    target
):

    workload = get_workload(workload_name)

    if not workload:

        return {
            "status": "failed",
            "message": "Workload not found"
        }

    if target == "docker":

        return docker_run(
            workload_name
        )

    elif target == "kubernetes":

        return kubernetes_run(
            workload_name
        )

    return {
        "status": "failed",
        "message": "Unsupported target"
    }