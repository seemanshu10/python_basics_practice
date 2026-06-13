import maya.cmds as cmds 

def populate_menu(*args):
    cmds.menu("dynamicMenu", edit = True, deleteAllItems= True)
    for i in range(5):
        cmds.menuItem(label = f"Option {i+1}", command = f"print('Option {i+1} selected')")
    
    
cmds.menu("dynamicMenu", label = "Dynamic Menu", parent = "MayaWindow", postMenuCommand = populate_menu)