import maya.cmds as cmds
MAIN_MENU = "Test"
SELECT_SUBMENU = "selectObjectSubMenu"

def populate_select_object_menu(*args):
    cmds.menu(SELECT_SUBMENU, edit = True, deleteAllItems= True)
    
    objects = cmds.ls(transforms=True) or []
 
    for obj in objects():
        cmds.menuItem(label = obj, parent = SELECT_SUBMENU, )
        
if cmds.menu(MAIN_MENU, exists=True):
    cmds.deleteUI(MAIN_MENU)
    
cmds.menu(MAIN_MENU, label = "Test_menu", parent = "MayaWindow", tearOff = True)
cmds.menuItem(SELECT_SUBMENU, parent = MAIN_MENU, subMenu = True)
cmds.menu(SELECT_SUBMENU, edit=True, postMenuCommand=populate_select_object_menu)

