import sys
import maya.cmds as cmds

sys.dont_write_bytecode = True
cmds.evalDeferred('import pb.general.startup')