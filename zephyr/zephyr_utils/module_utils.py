# Python Library Imports
import os
import sys
import logging
import click


from cookiecutter.main import cookiecutter


def create_module(project_name):
    """
    Purpose:
        Create a zephyr projecy
    Args:
        project - name of the project
    Returns:
        N/A
    """
    cookiecutter(
        "https://github.com/banjtheman/cookiecutter-zephyr-module",
        output_dir=f"{project_name}/modules/",
        extra_context={"project_name": project_name},
    )
