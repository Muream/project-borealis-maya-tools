import os

import maya.cmds as cmds
import maya.mel as mel
from mop.core.rig import Rig

def run():
    file_path = cmds.file(query=True, sceneName=True)

    rig = Rig()
    skel = rig.skeleton

    cmds.parent(skel[0], w=True)
    export_groups = cmds.listRelatives('GEO')
    export_geos = []
    for export_group in export_groups:
        geos = list(set(([cmds.listRelatives(m, p=True)[0] for m in cmds.listRelatives(export_group, ad=True, type='mesh')])))
        export_geos.extend(geos)
        cmds.parent(export_group, w=True)
    cmds.select(skel, replace=True)
    cmds.select(export_geos, add=True)

    release_path = os.path.dirname(file_path)
    scene_name = os.path.splitext(os.path.basename(file_path))[0]
    asset_name = scene_name.split('_')[1]
    version_number = scene_name.split('_')[3]
    fbx_name = '_'.join(["SK", asset_name, version_number]) + '.fbx'
    mel.eval("FBXExportSmoothingGroups -v true")
    mel.eval("FBXExportAnimationOnly -v false")
    mel.eval("FBXExportInputConnections -v false")
    mel.eval("FBXExportUpAxis z")
    command = 'FBXExport -f "{}" -s'.format(os.path.join(release_path, fbx_name)).replace('\\', '/')
    mel.eval(command)

    cmds.file(file_path, open=True, force=True)

if __name__ == '__main__':
    run()
