import typer

from cli.logger import logger
from cli.config_loader import load_config

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
def deploy():
    """Deploy workload"""

    logger.info("Deploy command executed")

    print("Deploying workload...")


@app.command()
def run():
    """Run workload"""

    logger.info("Run command executed")

    print("Running workload...")


@app.command()
def kpi():
    """Show KPIs"""

    logger.info("KPI command executed")

    print("Showing KPIs...")


@app.command()
def report():
    """Generate reports"""

    logger.info("Report command executed")

    print("Generating reports...")


@stack_app.command("list")
def list_stacks():
    """List software stacks"""

    logger.info("Listing software stacks")

    print("Listing software stacks...")


@workload_app.command("list")
def list_workloads():
    """List workloads"""

    logger.info("Listing workloads")

    print("Listing workloads...")


if __name__ == "__main__":
    app()