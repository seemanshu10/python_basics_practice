import maya.cmds as cmds

def create_cube(*args):
    cmds.polyCube(name = "NewCube")
    print("Cube Created")

def create_sphere(*args):
    cmds.polySphere(name = "NewSphere")
    print("Sphere Created")
    
def delete_selected(*args):
    selected_object = cmds.ls(sl = True, type = "transform")
    if selected_object:
        for object in selected_object:
            cmds.delete(object)
    else:
        print("Please select a Object to be deleted.")
        
def delete_history(*args):
    selected_object = cmds.ls(sl = True, type = "transform")
    if selected_object:
        for object in selected_object:
            cmds.delete(object, constructionHistory=True)
    else:
        print("Please select a Object to delete history.")
        
def freeze_transform(*args):
    cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=False)
    
def populate_menu(*args):
    cmds.menu(dynamic_menu, edit = True, deleteAllItems= True)
    for obj in sorted(cmds.ls(transforms=True)):
        cmds.menuItem(label=obj, parent=dynamic_menu)
    
    
MENU_VFX = "VFXUtilityTools"

if cmds.menu(MENU_VFX, exists = True):
    cmds.deleteUI(MENU_VFX, menu = True)
    
main_menu = cmds.menu(MENU_VFX, label = "VFX Utility", parent = "MayaWindow")
cmds.menuItem(label = "Modelling Tools", subMenu = True)
cmds.menuItem(label = "Create Sphere", command = create_cube)
cmds.menuItem(label = "Create Cube", command = create_sphere)

cmds.menuItem(label = "Selection", subMenu = True, parent = main_menu)
cmds.menuItem(label = "Delete Selected", command = delete_selected)
dynamic_menu = cmds.menuItem(label = "Select Dynamically", subMenu = True,postMenuCommand = populate_menu)

cmds.menuItem(label = "Scene Management", subMenu = True, parent = main_menu)
cmds.menuItem(label = "Freeze Transformation", command = freeze_transform)
cmds.menuItem(label = "Delete History", command = delete_history)

cmds.menuItem(label = "Export", parent = main_menu )
