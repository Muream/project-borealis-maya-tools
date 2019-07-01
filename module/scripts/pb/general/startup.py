import os
import site
import sys
import logging

import maya.cmds as cmds

logger = logging.getLogger(__file__)

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


logger.info("Loading Project Borealis tools.")
sys.dont_write_bytecode = True
init_assets_dir()
set_project()
build_menu()