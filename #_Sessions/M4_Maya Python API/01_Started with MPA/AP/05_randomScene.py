import maya.cmds as cmds
import random

for building in range(20):
    height = random.uniform(1.0, 10.0)

    cube, shape = cmds.polyCube(
        name=f"Building_{building}",
        height=height,
        width=1,
        depth=1
    )

    cmds.move(building * 1.2, 0, -6, cube)

    cmds.move(0, height / 2, 0, cube, relative=True)
    
for building in range(20):
    height = random.uniform(1.0, 10.0)

    cube, shape = cmds.polyCube(
        name=f"Building_{building}",
        height=height,
        width=1,
        depth=1
    )

    cmds.move(building * 1.2, 0, 6, cube)
    # move above grid 
    cmds.move(0, height / 2, 0, cube, relative=True)
    
cam1 = cmds.camera(name = "NewCam")[0]
cmds.setAttr("{}.rotateY".format(cam1), -90)
cmds.setAttr("{}.translateY".format(cam1),3)
cmds.lookThru(cam1)