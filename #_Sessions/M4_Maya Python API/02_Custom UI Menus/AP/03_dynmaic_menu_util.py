import maya.cmds as cmds
from functools import partial

MAIN_MENU = "utilityToolsMenu"
SELECT_SUBMENU = "selectObjectSubMenu"


def select_object(obj_name, *args):
    """Select the chosen object in Maya."""
    if cmds.objExists(obj_name):
        cmds.select(obj_name, replace=True)


def populate_select_object_menu(*args):
    """Rebuild the Select Object submenu every time it is opened."""

    # Remove existing menu items
    existing_items = cmds.menu(SELECT_SUBMENU, q=True, itemArray=True) or []
    for item in existing_items:
        cmds.deleteUI(item)

    # Get all scene transforms
    objects = cmds.ls(transforms=True) or []

    if not objects:
        cmds.menuItem(label="No Objects Found", parent=SELECT_SUBMENU, enable=False)
        return

    # Create menu item for each object
    for obj in sorted(objects):
        cmds.menuItem(
            label=obj,
            parent=SELECT_SUBMENU,
            command=partial(select_object, obj)
        )


def create_utility_tools_menu():
    """Create the Utility Tools menu."""

    if cmds.menu(MAIN_MENU, exists=True):
        cmds.deleteUI(MAIN_MENU)

    cmds.menu(
        MAIN_MENU,
        label="Utility Tools",
        parent="MayaWindow",
        tearOff=True
    )

    cmds.menuItem(
        SELECT_SUBMENU,
        label="Select Object",
        subMenu=True,
        parent=MAIN_MENU
    )

    cmds.menu(
        SELECT_SUBMENU,
        edit=True,
        postMenuCommand=populate_select_object_menu
    )


create_utility_tools_menu()