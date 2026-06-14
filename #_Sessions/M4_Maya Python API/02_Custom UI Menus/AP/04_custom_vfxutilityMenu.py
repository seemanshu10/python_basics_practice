import maya.cmds as cmds

def createCube(*args):
    cmds.polyCube(name = "NewCube")
    print("Cube Created")

def createSphere(*args):
    cmds.polySphere(name = "NewSphere")
    print("Sphere Created")

MENU_VFX = "VFXUtilityTools"

if cmds.menu(MENU_VFX, exists = True):
    cmds.deleteUI(MENU_VFX, menu = True)
    
main_menu = cmds.menu(MENU_VFX, label = "VFX Utility", parent = "MayaWindow")
cmds.menuItem(label = "Modelling Tools", subMenu = True)
cmds.menuItem(label = "Create Sphere", command = createSphere)
cmds.menuItem(label = "Create Cube", command = createCube)

cmds.menuItem(label = "Selection", subMenu = True, parent = main_menu)
cmds.menuItem(label = "Delete Selected")
cmds.menuItem(label = "Select Dynamically")

cmds.menuItem(label = "Scene Management", subMenu = True, parent = main_menu)
cmds.menuItem(label = "Freeze Transformation")
cmds.menuItem(label = "Delete History")

cmds.menuItem(label = "Export", command = createSphere, parent = main_menu )
