from pathlib import Path

from cli.config_loader import load_config

WORKLOADS_DIR = Path("workloads")


def get_workloads():

    workloads = []

    for workload_dir in WORKLOADS_DIR.iterdir():

        metadata_file = workload_dir / "metadata.yaml"

        if metadata_file.exists():

            workload = load_config(metadata_file)

            workloads.append(workload)

    return workloads


def get_workload(workload_name):

    for workload in get_workloads():

        if workload["name"] == workload_name:
            return workload

    return None