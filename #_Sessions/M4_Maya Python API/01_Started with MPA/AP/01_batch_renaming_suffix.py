import maya.cmds as cmds

obj_selected = cmds.ls(sl = True, type = "transform")
total_selected = len(obj_selected)
for object in obj_selected:
    
    cmds.rename(object ,'{}_Renamed'.format(object))

cmds.confirmDialog(title= "Renaming Complete", message = "{} Objects have been Renamed with suffix: _Renamed".format(total_selected), button=['OK'])