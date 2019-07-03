import os
import re

import maya.cmds as cmds


def set_assets_dir():
    assets_dir = cmds.fileDialog2(
        fileMode=3,
        okCaption='Browse',
        caption='raw-assets',
    )
    if assets_dir is not None:
        assets_dir = assets_dir[0]
        os.environ['PROJECT_BOREALIS_ASSETS'] = assets_dir


def assets_dir():
    return os.environ['PROJECT_BOREALIS_ASSETS']


def asset_dir():
    sceneName = cmds.file(query=True, sceneName=True)
    if not os.path.exists(sceneName):
        return
    directory = os.path.dirname(sceneName)
    return directory


def asset_file():
    sceneName = cmds.file(query=True, sceneName=True)
    if not os.path.exists(sceneName):
        return
    file_name = os.path.basename(sceneName)
    return file_name


def release_dir():
    directory = asset_dir()
    release = os.path.join(directory, 'release')
    if not os.path.exists(release):
        os.makedirs(release)
    return os.path.join(directory, 'release')


def old_dir():
    directory = asset_dir()
    old = os.path.join(directory, 'old')
    if not os.path.exists(old):
        os.makedirs(old)
    return old


def highest_version(path):
    highest_version = 0
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if not os.path.isfile(full_path):
            continue

        version = decompose_file_name(f)['version']
        if version > highest_version:
            highest_version = version

    return highest_version


def highest_release_version():
    return highest_version(release_dir())


def highest_work_version():
    return highest_version(asset_dir())


def decompose_file_name(file_name):
    regex = re.compile(r"^(?P<type>[a-zA-Z]*)_(?P<asset>[a-zA-Z]*)_((?P<step>[a-zA-Z]*)_)?(?P<description>.*)_v(?P<version>\d{3})\.(?P<extension>[a-zA-Z]*)$")
    match = regex.match(file_name)
    ret = {
        "type": match.group("type"),
        "asset": match.group("asset"),
        "step": match.group("step"),
        "description": match.group("description"),
        "version": int(match.group("version")),
        "extension": match.group("extension"),
    }
    return ret

def incremental_save():
    work_path = asset_dir()
    work_file = asset_file()
    full_work_file_path = os.path.join(work_path, work_file)
    full_old_file_path = os.path.join(work_path, old_dir(), work_file)
    decomposed = decompose_file_name(work_file)
    new_file = "{0}_{1}_{2}_{3}_v{4:0>3}.ma".format(
        decomposed["type"],
        decomposed["asset"],
        decomposed["step"],
        decomposed["description"],
        decomposed["version"] + 1,
    )
    full_new_file_path = os.path.join(work_path, new_file)
    cmds.file(rename=full_new_file_path)
    cmds.file(save=True, type='mayaAscii')

    os.rename(full_work_file_path, full_old_file_path)


if __name__ == "__main__":
    incremental_save()
