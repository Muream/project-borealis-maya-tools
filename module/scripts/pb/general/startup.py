import os
import site
import sys
import logging

import maya.cmds as cmds

logger = logging.getLogger(__file__)

from .menu import build_menu
from .assets import assets_dir, set_assets_dir


def add_vendor_to_path():
    pb_tools = os.path.dirname(__file__)
    vendor_path = os.path.join(pb_tools, "..", "..", "..", "vendor")
    site.addsitedir(vendor_path)


def set_playback_to_30fps():
    cmds.currentUnit(time="ntsc")  # 30fps
    cmds.playbackOptions(playbackSpeed=1)  # real-time playback

logger.info("Loading Project Borealis tools.")
add_vendor_to_path()
set_playback_to_30fps()
build_menu()