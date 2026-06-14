import maya.cmds as cmds

SHOT_VFX = "Shot_Management"

if cmds.menu(SHOT_VFX, exists = True):
    cmds.deleteUI(SHOT_VFX, menu = True)
    
main_menu = cmds.menu(SHOT_VFX, label = "Shot Utility", parent = "MayaWindow")
cmds.menuItem(label = "New Shot")
cmds.menuItem(label = "Shots")
cmds.menuItem(label = "Set Shot Camera")
cmds.menuItem(label = "Rename Shot")
cmds.menuItem(label = "Export Shot")

