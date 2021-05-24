# Python Library Imports
import click

# 3rd party imports
from cookiecutter.main import cookiecutter

# Project Imports
from zephyr.zephyr_utils import zephyr_utils


def create_module(project_name: str) -> None:
    """
    Purpose:
        Create a zephyr module
    Args:
        project - name of the project
    Returns:
        N/A
    """
    full_dir_path = cookiecutter(
        "https://github.com/banjtheman/cookiecutter-zephyr-module",
        output_dir=f"{project_name}/modules/",
        extra_context={"project_name": project_name},
    )

    # Add module to __init__.py
    init_path = f"{project_name}/modules/__init__.py"
    module_name = full_dir_path.split("/")[-1]
    import_text = f"from . import {module_name}\n"

    zephyr_utils.append_to_file(init_path, import_text)

    # update the config json with the modules
    zephyr_config = zephyr_utils.load_json(".zephyr/config.json")
    zephyr_config["modules"].append(module_name)
    zephyr_utils.save_json(".zephyr/config.json", zephyr_config)

    click.echo(f"Moudle {module_name} created")
