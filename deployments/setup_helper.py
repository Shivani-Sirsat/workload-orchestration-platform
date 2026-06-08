from deployments.prerequisites import (
    validate_prerequisites
)


def run_setup():

    results = validate_prerequisites()

    print("\nPlatform Setup Check\n")

    for tool, status in results.items():

        state = "FOUND" if status else "MISSING"

        print(f"{tool}: {state}")

    print("\nRecommended Actions:\n")

    if not results["docker"]:

        print(
            "Install Docker Desktop:"
        )
        print(
            "https://www.docker.com/products/docker-desktop/"
        )
        print()

    if not results["kubectl"]:

        print(
            "Install kubectl:"
        )
        print(
            "https://kubernetes.io/docs/tasks/tools/"
        )
        print()

    print("Setup validation complete.")