# Python Library Imports
import os
import sys
import logging
import click


# Local Python Library Imports
from zephyr.zephyr_state.zephyr_state import ZephyrState
from zephyr.zephyr_utils import (
    zephyr_utils,
)


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
@click.option("--project", help="Project to create", required=True)
def init_command(project: str) -> None:
    """Create and initialize zephyr folder"""
    """
    Purpose:
        Create and initialize zephyr project
    Args:
        folder (String) - Folder to create
    Returns:
        N/A
    """

    LOGGER.info(f"Init project {project}")


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


if __name__ == "__main__":

    try:
        setup_zephyr_cli()
    except Exception as error:
        print(f"{os.path.basename(__file__)} failed due to error: {error}")
        raise error
