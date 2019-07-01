import os

import maya.cmds as cmds

from config import write_config, get_config


def set_assets_dir():
    config = get_config()
    assets_dir = cmds.fileDialog2(
        fileMode=3,
        okCaption='Browse',
        caption='raw-assets',
    )
    if assets_dir is not None:
        assets_dir = assets_dir[0]
        config['assets_dir'] = assets_dir
        write_config(config)


def get_assets_dir():
    config = get_config()
    assets_dir = config.get('assets_dir')

    return assets_dir


def current_asset_dir():
    sceneName = cmds.file(query=True, sceneName=True)
    if not os.path.exists(sceneName):
        return
    asset_dir = os.path.dirname(sceneName)
    return asset_dir


def release_dir():
    asset_dir = current_asset_dir()
    return os.path.join(asset_dir, 'release')


def old_dir():
    asset_dir = current_asset_dir()
    return os.path.join(asset_dir, 'old')
