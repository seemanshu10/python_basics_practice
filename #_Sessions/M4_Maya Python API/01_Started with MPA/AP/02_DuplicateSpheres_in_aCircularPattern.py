import maya.cmds as cmds 
import math 

original_object = cmds.ls(sl = True, type = "transform")[0]
if not original_object:
    print("Please select a Object before running the script.")
    
number_of_duplicates = 16
radius = 10.0 

group_name = "Circular_Spheres_Group" 

if cmds.objExists(group_name):
    cmds.delete(group_name)
    
group_create = cmds.group(empty = True, name = group_name)

for i in range(number_of_duplicates):
    dup_object = cmds.duplicate(original_object, n = "Sphere")
    cmds.parent(dup_object, group_name)
    
    angle = (2 * math.pi / number_of_duplicates) * i

    x = radius * math.cos(angle)
    y = 0
    z = radius * math.sin(angle)
    
    cmds.move(x, y , z)
    