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
        "command": "import general.assets;general.assets.set_assets_dir()",
        "label": "Set Assets Directory",
        "parent": "general",
    },
    {
        "name": "animation",
        "label": "Animation",
        "subMenu": True,
    },
    {
        "name": "publish",
        # "command": "import mop;mop.incremental_save()",
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
