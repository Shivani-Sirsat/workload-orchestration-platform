from cli.workload_registry import get_workload

from deployments.docker import deploy as docker_deploy
from deployments.kubernetes import deploy as kubernetes_deploy
from deployments.baremetal import deploy as baremetal_deploy
from deployments.cloud import deploy as cloud_deploy

from deployments.prerequisites import (
    validate_prerequisites
)


def deploy_workload(workload_name, target):

    workload = get_workload(workload_name)

    if not workload:

        return {
            "status": "failed",
            "message": "Workload not found"
        }

    if target not in workload["supported_targets"]:

        return {
            "status": "failed",
            "message": f"Target {target} not supported"
        }

    validation = validate_prerequisites()

    if target == "docker":

        if not validation["docker"]:

            return {
                "status": "failed",
                "message": "Docker not installed"
            }

        docker_deploy(workload_name)

    elif target == "kubernetes":

        if not validation["kubectl"]:

            return {
                "status": "failed",
                "message": "kubectl not installed"
            }

        kubernetes_deploy(workload_name)

    elif target == "baremetal":

        baremetal_deploy(workload_name)

    elif target == "cloud":

        cloud_deploy(workload_name)

    return {
        "status": "success",
        "workload": workload_name,
        "stack": workload["stack"],
        "target": target
    }