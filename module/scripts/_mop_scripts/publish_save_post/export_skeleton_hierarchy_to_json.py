import os
import maya.cmds as cmds
from mop.dag import hierarchy_to_dict
import json


target_asset_type = ['weapon']


def run():
    parent = 'root'
    hierarchy_dict = {}
    hierarchy_to_dict(parent, hierarchy_dict)

    file_path = cmds.file(query=True, sceneName=True)

    release_path = os.path.dirname(file_path)

    scene_name = os.path.basename(file_path)
    json_name = scene_name.split('.')[0] + '.json'
    json_path = os.path.join(release_path, json_name)

    with open(json_path, 'w') as f:
        f.write(json.dumps(hierarchy_dict, indent=4))



if __name__ == '__main__':
    run(from_release=True)
