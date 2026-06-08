from pathlib import Path

from cli.config_loader import load_config

STACKS_DIR = Path("stacks")


def get_stacks():

    stacks = []

    for stack_dir in STACKS_DIR.iterdir():

        metadata_file = stack_dir / "metadata.yaml"

        if metadata_file.exists():

            stack = load_config(metadata_file)

            stacks.append(stack)

    return stacks


def get_stack(stack_name):

    for stack in get_stacks():

        if stack["name"] == stack_name:
            return stack

    return None