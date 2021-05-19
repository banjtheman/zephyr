# Python Library Imports
import os
import sys
import logging
import click


from cookiecutter.main import cookiecutter

from zephyr.zephyr_utils import zephyr_utils


def create_module(project_name):
    """
    Purpose:
        Create a zephyr projecy
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

    # from . import my_module
    # append import to __init.py

    # Add module to __init__.py
    init_path = f"{project_name}/modules/__init__.py"
    module_name = full_dir_path.split("/")[-1]
    import_text = f"from . import {module_name}\n"

    zephyr_utils.append_to_file(init_path, import_text)
