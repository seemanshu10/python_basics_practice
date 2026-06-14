import maya.cmds as cmds
import math 
import random 

def rename_suffix(*args):
    obj_selected = cmds.ls(sl = True, type = "transform")
    total_selected = len(obj_selected)
    for object in obj_selected:
        
        cmds.rename(object ,'{}_Renamed'.format(object))
    
    cmds.confirmDialog(title= "Renaming Complete", message = "{} Objects have been Renamed with suffix: _Renamed".format(total_selected), button=['OK'])

def circle_placement(*args):
    

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
        
def random_placement(*args):
    
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
               
def random_color(*args):
    
    number_of_duplicates = 25
    group_name = "Random_Spheres_Group"
    
    group_create = cmds.group(empty=True, name=group_name)
    
    for i in range(number_of_duplicates):
    
        sphere_obj = cmds.polySphere(name=f"sphere_{i+1}")[0]
    
        # Random position
        x = random.uniform(-10.0, 10.0)
        y = random.uniform(-10.0, 10.0)
        z = random.uniform(-10.0, 10.0)
    
        cmds.move(x, y, z, sphere_obj)
    
        # Create  Lambert shader
        shader = cmds.shadingNode("lambert", asShader=True,name=f"Lambert_{i+1}")
    
        # Random RGB color
        r = random.random()
        g = random.random()
        b = random.random()
    
        cmds.setAttr(shader + ".color", r, g, b,type="double3")
        sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{shader}SG")
        cmds.connectAttr(shader + ".outColor", sg + ".surfaceShader", force=True)
        cmds.sets(sphere_obj,edit=True,forceElement=sg)
        cmds.parent(sphere_obj, group_create)
        
        cmds.setKeyframe(sphere_obj, attribute="translateX", time=1, value=0)
        cmds.setKeyframe(sphere_obj, attribute="translateX", time=24, value=x)
        cmds.setKeyframe(sphere_obj, attribute="translateX", time=48, value=0)
    
        cmds.setKeyframe(sphere_obj, attribute="translateY", time=1, value=0)
        cmds.setKeyframe(sphere_obj, attribute="translateY", time=24, value=y)
        cmds.setKeyframe(sphere_obj, attribute="translateY", time=48, value=0)
    
        cmds.setKeyframe(sphere_obj, attribute="translateZ", time=1, value=0)
        cmds.setKeyframe(sphere_obj, attribute="translateZ", time=24, value=z)
        cmds.setKeyframe(sphere_obj, attribute="translateZ", time=48, value=0)
        
    print("Created {} sphere_objects with unique Lambert shaders and random colors.".format(number_of_duplicates))
    
MAIN_MENU = "UtilityMenu"

def custom_main_menu():
    if cmds.menu(MAIN_MENU, exists = True):
        cmds.deleteUI(MAIN_MENU)

    main_menu = cmds.menu(MAIN_MENU, label = "Utility Tools", parent = "MayaWindow")
    cmds.menuItem(label = "Rename", command = rename_suffix)
    cmds.menuItem(label = "Spehres_Circular", command = circle_placement )
    cmds.menuItem(label = "Random Placement", command = random_placement)
    cmds.menuItem(label = "Random Color", command = random_color)

custom_main_menu()
