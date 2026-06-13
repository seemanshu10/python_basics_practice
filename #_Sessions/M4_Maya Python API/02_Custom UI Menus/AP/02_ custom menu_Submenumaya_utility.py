import maya.cmds as cmds 

def createSphere(*args):
    cmds.polySphere(name = "NewSphere")
    print("Sphere Created")

def createCube(*args):
    cmds.polyCube(name = "NewCube")
    print("Cube Created")
    
def delete_selected(*args):
    selected_object = cmds.ls(sl = True, type = "transform")[0]
    if selected_object:
        cmds.delete(selected_object)
        print("Please select a Object to be deleted.")

MENU_NAME = "utilityToolsMenu"

if cmds.menu(MENU_NAME, exists = True):
    cmds.deleteUI(MENU_NAME, menu = True)
    
cmds.menu(MENU_NAME, label = "Utility Tools", parent = "MayaWindow")
cmds.menuItem(label = "Create Sphere", command = createSphere)
cmds.menuItem(label = "Print Message", command = 'print("Welcome to Utility Tools!")') 

cmds.menuItem(label = "Object Tools", subMenu = True)
cmds.menuItem(label = "Create Cube", command = createCube)
cmds.menuItem(label = "Delete Selected", command = delete_selected) 
   