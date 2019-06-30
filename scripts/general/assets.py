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
