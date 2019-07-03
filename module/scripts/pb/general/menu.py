import maya.cmds as cmds

PB_MENU = "PB_MENU"

MENU_ITEMS = [
    {
        "name": "general",
        "label": "General",
        "subMenu": True,
    },
    {
        "name": "incremental_save",
        # "command": "import mop;mop.incremental_save()",
        "label": "Incremental Save",
        "parent": "general",
    },
    {
        "name": "set_assets_directory",
        "command":
        "import pb.general.assets;pb.general.assets.set_assets_dir()",
        "label": "Set Assets Directory",
        "parent": "general",
    },
    {
        "name": "reload_pb_tools",
        "command": "import pb.general;pb.general.reload_pb_tools()",
        "label": "Reload Tools",
        "parent": "general",
    },
    {
        "name": "animation",
        "label": "Animation",
        "subMenu": True,
    },
    {
        "name": "studiolib",
        "command": "from pb.animation.studiolib import open_shared_lib;open_shared_lib()",
        "label": "Open Studio Library",
        "parent": "animation",
    },
    {
        "name": "publish",
        "command": "from pb.animation.publish import publish;publish()",
        "label": "Publish",
        "parent": "animation",
    },
]


def build_menu():
    if not cmds.menu(PB_MENU, query=True, exists=True):
        cmds.menu(PB_MENU,
                  label="Project Borealis",
                  parent="MayaWindow",
                  tearOff=True)

    for data in MENU_ITEMS:
        name = data.pop("name")
        subMenu = data.pop("subMenu", False)
        parent = data.pop("parent", PB_MENU)
        cmds.menuItem(name, parent=parent, subMenu=subMenu, **data)
