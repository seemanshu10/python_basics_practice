import maya.cmds as cmds 
import random 

number_of_duplicates = 25
group_name = "Random_Spheres_Group" 

if cmds.objExists(group_name):
    cmds.delete(group_name)
    
group_create = cmds.group(empty = True, name = group_name)

for i in range(number_of_duplicates):
    random_object = cmds.polySphere(name = "Sphere")
    cmds.parent(random_object, group_create)
    
    x = random.uniform(-10.0, 10.0)
    y = random.uniform(-10.0, 10.0)
    z = random.uniform(-10.0, 10.0)
    
    cmds.move(x, y, z)
    
    