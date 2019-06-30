import os
import site
import sys
import logging

import maya.cmds as cmds

logger = logging.getLogger()

# pulling the latest changes needs to be done before importing anything from the tools.
import subprocess


def pull_latest_changes():
    subprocess.check_output(["git", "pull"])


try:
    pull_latest_changes()
except Exception as e:
    logger.error(e)

from .config import get_config, write_config
from .menu import build_menu
from .assets import get_assets_dir, set_assets_dir


def init_assets_dir():
    assets_dir = get_assets_dir()
    if assets_dir is None:
        res = cmds.confirmDialog(
            title='PB tools',
            message='Please browse to the raw-asset directory',
            button=['Browse', 'Cancel'],
            defaultButton='Browse',
            cancelButton='Cancel',
        )
        if res == 'Browse':
            set_assets_dir()


def set_project():
    assets_dir = get_assets_dir()
    if assets_dir:
        cmds.workspace(directory=assets_dir)


def add_vendor_to_path():
    pb_tools = os.path.dirname(__file__)
    site.addsitedir(os.path.join(pb_tools, 'vendor'))


sys.dont_write_bytecode = True
init_assets_dir()
set_project()
build_menu()