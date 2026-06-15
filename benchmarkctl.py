import typer

from cli.logger import logger
from cli.config_loader import load_config
from execution.report_reader_db import (
    generate_report
)
from execution.result_reader import (
    load_result
)
from execution.execution_engine import (
    execute_workload
)
from deployments.prerequisites import (
    validate_prerequisites
)
from execution.history_reader_db import (
    load_history
)
from deployments.deployment_engine import deploy_workload
from cli.stack_registry import (
    get_stacks,
    get_stack
)
from deployments.setup_helper import (
    run_setup
)

from execution.compare_reader_db import (
    load_compare_data
)

from cli.workload_registry import (
    get_workloads,
    get_workload
)

app = typer.Typer(
    help="Workload Orchestration Platform"
)

stack_app = typer.Typer(
    help="Software Stack Management"
)

workload_app = typer.Typer(
    help="Workload Management"
)

app.add_typer(stack_app, name="stack")
app.add_typer(workload_app, name="workload")


@app.command()
def list():
    """List registered entities"""

    logger.info("Listing platform information")

    config = load_config("configs/platform.yaml")

    print(config)


@app.command()
def build():
    """Build workload"""

    logger.info("Build command executed")

    print("Building workload...")


@app.command()
def deploy(
    workload_name: str,
    target: str
):

    logger.info(
        f"Deploying {workload_name} to {target}"
    )

    result = deploy_workload(
        workload_name,
        target
    )

    if result["status"] == "failed":

        print(result["message"])
        return

    print(
        f"Deploying workload: "
        f"{result['workload']}"
    )

    print(
        f"Using stack: "
        f"{result['stack']}"
    )

    print(
        f"Target: "
        f"{result['target']}"
    )

    print("\nDeployment successful")


@app.command()
def run(
    workload_name: str,
    target: str
):

    logger.info(
        f"Executing {workload_name} on {target}"
    )

    result = execute_workload(
        workload_name,
        target
    )

    if result["status"] == "failed":

        print(
            result["message"]
        )

        return

    print(
        "\nBenchmark KPIs\n"
    )

    for key, value in result["output"].items():

        print(
            f"{key}: {value}"
        )


@app.command()
def kpi(
    workload_name: str
):

    result = load_result(
        workload_name
    )

    if not result:

        print(
            "No KPI found"
        )

        return

    print(
        "\nStored KPIs\n"
    )

    for key, value in result.items():

        print(
            f"{key}: {value}"
        )

@app.command()
def history(
    workload_name: str
):

    history = load_history(
        workload_name
    )

    if not history:

        print(
            "No history found"
        )

        return

    print(
        f"\nExecution History: {workload_name}\n"
    )

    for run in history:

        print(
            f"Run: {run['run']}"
        )

        for key, value in run["kpis"].items():

            print(
                f"  {key}: {value}"
            )

        print()

@app.command()
def compare(
    workload_name: str
):

    previous, latest = (
        load_compare_data(
            workload_name
        )
    )

    if not previous:

        print(
            "Need at least 2 runs"
        )

        return

    print(
        "\nComparing Latest Two Runs\n"
    )

    print("Latest Run:")

    for key, value in latest.items():

        print(
            f"  {key}: {value}"
        )

    print("\nPrevious Run:")

    for key, value in previous.items():

        print(
            f"  {key}: {value}"
        )

    print("\nDifference:")

    for key in latest:

        if key not in previous:

            print(
                f"  {key}: N/A"
            )

            continue

        old_value = previous[key]
        new_value = latest[key]

        if not isinstance(
            old_value,
            (int, float)
        ):

            print(
                f"  {key}: N/A"
            )

            continue

        if old_value == 0:

            print(
                f"  {key}: N/A"
            )

            continue

        diff = (
            (
                new_value - old_value
            )
            / old_value
        ) * 100

        print(
            f"  {key}: {diff:.2f}%"
        )

@app.command()
def report(
    workload_name: str
):

    runs = generate_report(
        workload_name
    )

    if not runs:

        print(
            "No report data found"
        )

        return

    latest = runs[-1]

    print(
        f"\nBenchmark Report: {workload_name}\n"
    )

    print(
        f"Total Runs: {len(runs)}"
    )

    print(
        f"Target: {latest['target']}"
    )

    print(
        f"Latest Run: {latest['timestamp']}"
    )

    numeric_fields = {}

    #
    # Discover all numeric KPIs
    #

    for run in runs:

        for key, value in run.items():

            if isinstance(
                value,
                (int, float)
            ):

                if key not in numeric_fields:

                    numeric_fields[key] = []

    #
    # Collect KPI values
    #

    for run in runs:

        for key in numeric_fields:

            if key not in run:

                continue

            numeric_fields[key].append(
                run[key]
            )

    print(
        "\nKPI Summary"
    )

    for key, values in numeric_fields.items():

        if not values:

            continue

        latest_value = values[-1]

        if "latency" in key.lower():

            best_value = min(values)

        else:

            best_value = max(values)

        average_value = (
            sum(values)
            / len(values)
        )

        print(
            f"\n{key}"
        )

        print(
            f"  Latest : {latest_value:.2f}"
        )

        print(
            f"  Best   : {best_value:.2f}"
        )

        print(
            f"  Average: {average_value:.2f}"
        )

@app.command()
def validate():

    results = validate_prerequisites()

    print("\nSystem Validation\n")

    for tool, status in results.items():

        state = "FOUND" if status else "MISSING"

        print(f"{tool}: {state}")

@app.command()
def setup():

    run_setup()


@stack_app.command("list")
def list_stacks():

    logger.info("Listing software stacks")

    stacks = get_stacks()

    for stack in stacks:
        print(stack["name"])


@stack_app.command("show")
def show_stack(stack_name: str):

    stack = get_stack(stack_name)

    if not stack:
        print("Stack not found")
        return

    print(f"Name: {stack['name']}")
    print(f"Version: {stack['version']}")
    print(f"Description: {stack['description']}")

    print("\nSupported Targets:")

    for target in stack["supported_targets"]:
        print(f"- {target}")


@workload_app.command("list")
def list_workloads():

    logger.info("Listing workloads")

    workloads = get_workloads()

    for workload in workloads:
        print(workload["name"])


@workload_app.command("show")
def show_workload(workload_name: str):

    workload = get_workload(workload_name)

    if not workload:
        print("Workload not found")
        return

    print(f"Name: {workload['name']}")
    print(f"Stack: {workload['stack']}")
    print(f"Description: {workload['description']}")

    print("\nSupported Targets:")

    for target in workload["supported_targets"]:
        print(f"- {target}")


if __name__ == "__main__":
    app()