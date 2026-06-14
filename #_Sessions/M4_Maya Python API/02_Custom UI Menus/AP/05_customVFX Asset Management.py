import maya.cmds as cmds

def group_selected(*args):
    obj_selected = cmds.ls(sl = True,type = "transform")
    if not obj_selected:
        print("Please select a transform Object before running the script.")
    
    group_create = cmds.group(name = "Group")
    
# rename transfroms 
def rename_selected(*args):
    obj_selected = cmds.ls(sl = True,type = "transform")
    total_selected = len(obj_selected)
    
    if not obj_selected:
        print("Please select a transdorm Object before running the script.")
        
    for object in obj_selected:
        cmds.rename(object ,'{}_Renamed'.format(object))
    
    cmds.confirmDialog(title= "Renaming Complete", message = "{} Objects have been Renamed with suffix: _Renamed".format(total_selected), button=['OK'])    

MENU_NAME = "vfxAssetManagementMenu"

def create_main_menu():
    if cmds.menu(MENU_NAME, exists=True):
        cmds.deleteUI(MENU_NAME)

    cmds.menu(MENU_NAME,label = "VFX Management", parent = "MayaWindow", tearOff=True)
    cmds.menuItem(label = "Rename Selected", command = rename_selected)
    cmds.menuItem(label = "Group Selected", command = group_selected)
    cmds.menuItem(label = "Parent Selected")
    cmds.menuItem(label = "Layers Selected")
    cmds.menuItem(label = "Export Selected")

create_main_menu()