import os
import maya.cmds as cmds
import logging
import re

# logger = logging.getLogger(__name__)
asset_types = ['character', 'prop', 'weapon']  # List of asset types (str)
scene_path = cmds.file(query=True, sceneName=True)
if scene_path:
    raw_asset_dir = re.search(r"(.*\/raw-assets\/)", scene_path).groups()[0]
    project_scripts_dir = {"relative": True, "path": os.path.join(raw_asset_dir, "_mop_scripts")}
else:
    raw_asset_dir = None
    project_scripts_dir = None

def get_asset_type():
    """Get the asset type of the asset currently open in maya.
    The asset type is derived from the file path

    :rtype: str
    """
    scene_dir = os.path.dirname(cmds.file(query=True, sceneName=True))
    if not scene_dir:
        return
    if not 'raw-assets' in scene_dir:
        # logger.error("The current scene isn't located in the raw-assets directory (or one of its children)")
        return
    else:
        regex = re.search(r"raw-assets/(?P<type>[^/]+)/", scene_dir)
        return regex.groups()[0]

__all__ = ["project_scripts_dir", "get_asset_type"]

