import maya.cmds as cmds

target_asset_type = ['weapon']

def run():
    character_joints = ['pelvis', 'spine_01', 'spine_02', 'spine_03', 'clavicle_r', 'upperarm_r', 'lowerarm_r', 'hand_r']
    parent = 'root'
    weapon_joints = cmds.listRelatives('root')

    for joint in character_joints:
        if not cmds.objExists(joint):
            joint = cmds.createNode('joint', name=joint)
            cmds.parent(joint, parent)
            parent = joint

    for joint in weapon_joints:
        cmds.parent(joint, parent)



if __name__ == '__main__':
    # should be ran from the release file
    run()
