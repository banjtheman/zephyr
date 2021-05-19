# Python Library Imports
import os
import sys
import logging
import click


# Local Python Library Imports
from zephyr.zephyr_state.zephyr_state import ZephyrState
from zephyr.zephyr_utils import zephyr_utils, init_utils, module_utils


# Setup Zephyr Logging
LOGLEVEL = logging.INFO
logging.basicConfig(
    format="%(asctime)s | %(levelname)s : %(message)s",
    level=LOGLEVEL,
    stream=sys.stdout,
)
LOGGER = logging.getLogger("zephyr-log")


@click.group(invoke_without_command=False)
@click.version_option("0.0.1")
@click.pass_context
def zephyr_cli(cli_context: click.Context) -> None:
    """
    A Scalable I/O Pipeline Builder
    """

    cli_context.obj = ZephyrState()

    return None


@click.command("init")
# @click.option("--project", help="Project to create", required=True)
def init_command() -> None:
    """Create and initialize zephyr folder"""
    """
    Purpose:
        Create and initialize zephyr project
    Args:
        N/A
    Returns:
        N/A
    """

    LOGGER.info(f"initializing project...")
    init_utils.create_project()


# Command Group
@zephyr_cli.group("module")
def module_commands():
    """Module related commands"""
    pass


@module_commands.command(name="create", help="creates new module")
def module_create() -> None:
    """Create and initialize zephyr folder"""
    """
    Purpose:
        Create and initialize zephyr project
    Args:
        N/A
    Returns:
        N/A
    """

    # Check if in project
    if zephyr_utils.check_if_in_project():
            
        # get module json
        project_json = zephyr_utils.load_json(".zephyr/config.json")
        project_name = project_json["project_name"]

        LOGGER.info(f"Creating module...")
        module_utils.create_module(project_name)


def setup_zephyr_cli() -> None:
    """
    Purpose:
        Build Command Groups for Zephyr CLI.
    Args:
        N/A
    Returns:
        N/A
    """

    # zephyr Commands
    zephyr_cli.add_command(init_command)
    module_commands.add_command(module_create)


if __name__ == "__main__":

    try:
        setup_zephyr_cli()
    except Exception as error:
        print(f"{os.path.basename(__file__)} failed due to error: {error}")
        raise error
