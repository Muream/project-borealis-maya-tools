import os

import maya.cmds as cmds
import maya.mel as mel

import pb.general.assets as assets


def create_export_skeleton():
    rigs = cmds.ls("*:RIG")

    character_rig = None
    weapon_rig = None
    for rig in rigs:
        if rig.startswith('ch'):
            character_rig = rig
        elif rig.startswith('wp'):
            weapon_rig = rig

    character_namespace = character_rig.rpartition(':')[0]

    character_skel_group = cmds.listConnections(character_rig + '.skeleton_group', source=True)[0]
    character_root_joint = cmds.listRelatives(character_skel_group)[0]
    export_skeleton = cmds.duplicate(character_root_joint)
    cmds.parent(export_skeleton[0], world=True)

    for joint in export_skeleton:
        character_joint = character_namespace + ':' + joint
        cmds.parentConstraint(character_joint, joint)

    if weapon_rig is not None:
        weapon_namespace = weapon_rig.rpartition(':')[0]
        for joint in export_skeleton:
            weapon_joint = weapon_namespace + ':' + joint
            if joint.startswith('weapon') and cmds.objExists(weapon_joint):
                old_constraint = cmds.listRelatives(joint, type='constraint')
                cmds.delete(old_constraint)
                cmds.parentConstraint(weapon_joint, joint)


def delete_export_skeleton():
    root = "|root"
    if cmds.objExists(root):
        cmds.delete(root)


def release_fbx_name(version):
    work_file = assets.asset_file()
    highest_version = assets.highest_release_version()
    decomposed = assets.decompose_file_name(work_file)
    f = "A_{0}_{1}_v{2:0>3}.fbx".format(
        decomposed['asset'],
        decomposed['description'],
        version,
    )
    return f

def release_scene_name(version):
    work_file = assets.asset_file()
    highest_version = assets.highest_release_version()
    decomposed = assets.decompose_file_name(work_file)
    f = "{0}_{1}_{2}_{3}_v{4:0>3}.ma".format(
        decomposed["type"],
        decomposed["asset"],
        decomposed["step"],
        decomposed["description"],
        version,
    )
    return f


def export_animation(version):
    release_dir = assets.release_dir()
    file_name = release_fbx_name(version)
    fbx_path = os.path.join(release_dir, file_name).replace("\\", "/")

    skeleton = cmds.listRelatives(
        '|root', allDescendents=True, type='joint'
    )
    skeleton.insert(0, "|root")
    cmds.select(skeleton, replace=True)

    mel.eval("FBXExportBakeComplexAnimation  -v true")
    mel.eval("FBXExportInputConnections -v false")
    mel.eval("FBXExportUpAxis z")
    command = 'FBXExport -f "{}" -s'.format(fbx_path)
    mel.eval(command)

def save_release_scene(version):
    release_dir = assets.release_dir()
    file_name = release_scene_name(version)
    full_path = os.path.join(release_dir, file_name)

    cmds.file(rename=full_path)
    cmds.file(save=True, type='mayaAscii')


def publish():
    new_version = assets.highest_release_version() + 1
    assets.incremental_save()
    create_export_skeleton()
    export_animation(version=new_version)
    delete_export_skeleton()
    save_release_scene(version=new_version)

if __name__ == "__main__":
    create_export_skeleton()
