import maya.cmds as cmds

MAIN_MENU = "Test"
SELECT_SUBMENU = "selectObjectSubMenu"

def populate_select_object_menu(*args):
    cmds.menu(SELECT_SUBMENU, edit=True, deleteAllItems=True)

    objects = cmds.ls(transforms=True) or []

    for obj in objects:
        cmds.menuItem(label=obj, parent=SELECT_SUBMENU, command=lambda _, o=obj: cmds.select(o))


if cmds.menu(MAIN_MENU, exists=True):
    cmds.deleteUI(MAIN_MENU)
cmds.menu(MAIN_MENU, label="Test_menu", parent="MayaWindow", tearOff=True)
cmds.menuItem(SELECT_SUBMENU, label="Select Object", parent=MAIN_MENU, subMenu=True)

populate_select_object_menu()