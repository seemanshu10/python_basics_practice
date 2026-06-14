import maya.cmds as cmds
import random

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

    # Create shading group
    sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{shader}SG")

    # Connect shader to shading group
    cmds.connectAttr(shader + ".outColor", sg + ".surfaceShader", force=True)

    # Assign shader to sphere_obj
    cmds.sets(sphere_obj,edit=True,forceElement=sg)

    # Parent under group
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