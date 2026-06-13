import maya.cmds as cmds 

menu_title = "Utility Tools"

if cmds.menu(menu_title, exists = True):
    cmds.deleteUI(menu_title, menu = True)
    
cmds.menu(menu_title, label = menu_title, parent = "MayaWindow")
cmds.menuItem(label = "Create Sphere", command = 'cmds.polySphere()')
cmds.menuItem(label = "Print Message", command = 'print("Welcome to Utility Tools!")')