# Python Library Imports
import logging
import os
import json
from subprocess import Popen
from typing import Type, Union, Dict, Any

# Local Python Library Imports
from zephyr.zephyr_config.config import Config


def check_if_in_project() -> bool:
    """
    Purpose:
       check if in zephyr project
    Args:
        N/A
    Returns:
        status (Boolean): False if not in zephyr project, True if in zephyr project
    """
    # check if folder exisit
    if os.path.exists(".zephyr/config.json"):
        # we should only check this file, in a git project if you delete .git
        # you are no longer in a git project we will follow that example
        status = True
    else:
        logging.info("Not inside Zephyr Project")
        logging.info("run `zephyr init and retry")
        status = False
    return status


def get_logger(name: str, log_level: int) -> logging.Logger:
    """
    Purpose:
        Load logger object
    Args:
        name (String): name of log
        log_level(Int): Level for log
    Returns:
        logger (Logger obj): Logger object
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Prevent logging from propagating to the root logger
        logger.propagate = False
        console = logging.StreamHandler()
        logger.addHandler(console)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s -  %(name)s - %(message)s"
        )
        console.setFormatter(formatter)
        logger.setLevel(log_level)
    return logger


def load_configs() -> Type[Config]:
    """
    Purpose:
        Load configuration object
    Args:
        environment (String): Environment to get configs for
    Returns:
        config (Config obj): Configuration object
    """

    return Config


def load_json(path_to_json: str) -> Dict[str, Any]:
    """
    Purpose:
        Load json files
    Args:
        path_to_json (String): Path to  json file
    Returns:
        Conf: JSON file if loaded, else None
    """
    try:
        with open(path_to_json, "r") as config_file:
            conf = json.load(config_file)
            return conf

    except Exception as error:
        logging.error(error)
        raise TypeError("Invalid JSON file")


def save_json(json_path: str, json_data: Any) -> None:
    """
    Purpose:
        Save json files
    Args:
        path_to_json (String): Path to  json file
        json_data: Data to save
    Returns:
        N/A
    """
    try:
        with open(json_path, "w") as outfile:
            json.dump(json_data, outfile)
    except Exception as error:
        raise OSError(error)
