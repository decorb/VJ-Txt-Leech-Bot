# utils.py — Helper Functions

import os
import shutil
import logging

from vars import DOWNLOAD_DIR

logger = logging.getLogger(__name__)


def create_download_dir():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)


def clean_up(file_path: str):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        logger.error(f"Error cleaning up {file_path}: {e}")


def get_file_extension(name: str):
    return os.path.splitext(name)[-1].lower()
