import maya.cmds as cmds

a = cmds.ls(selection=True)

print(a)

cmds.rename(a[0], "derp")
cmds.rename(a[1], "alisdfgöasiudfhwer")