import os
import site
import sys
import logging

import maya.cmds as cmds

logger = logging.getLogger(__file__)

from .config import get_config, write_config
from .menu import build_menu
from .assets import assets_dir, set_assets_dir


def add_vendor_to_path():
    pb_tools = os.path.dirname(__file__)
    site.addsitedir(os.path.join(pb_tools, "..", "vendor"))


logger.info("Loading Project Borealis tools.")
add_vendor_to_path()
build_menu()