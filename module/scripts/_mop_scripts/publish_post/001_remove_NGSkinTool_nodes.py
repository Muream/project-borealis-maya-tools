import maya.cmds as cmds


def run():
	cmds.delete(cmds.ls(type='ngSkinLayerData'))