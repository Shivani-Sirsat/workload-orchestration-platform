import typer

from cli.logger import logger
from cli.config_loader import load_config
from execution.result_reader import (
    load_result
)
from execution.execution_engine import (
    execute_workload
)
from deployments.prerequisites import (
    validate_prerequisites
)
from execution.history_reader import (
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

from execution.compare_reader import (
    load_latest_two_runs
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
        load_latest_two_runs(
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

        old_value = previous[key]
        new_value = latest[key]

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
def report():
    """Generate reports"""

    logger.info("Report command executed")

    print("Generating reports...")

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