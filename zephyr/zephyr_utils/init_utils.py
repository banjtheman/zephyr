# Python Library Imports
import os
import sys
import logging
import click


from cookiecutter.main import cookiecutter


def create_project():
    """
    Purpose:
        Create a zephyr projecy
    Args:
        project - name of the project
    Returns:
        N/A
    """
    cookiecutter("https://github.com/banjtheman/cookiecutter-zephyr")
