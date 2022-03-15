# OBJECT RENAMER

import maya.cmds as cmds


#BEGIN FUNCTION DEFINITIONS
def renameObject (*args):
    a = cmds.ls(sl=True)
    txt = cmds.textField(txt_field, q=True, tx=True)

    cmds.rename(a[0], txt)
    cmds.confirmDialog(ich='information', message='Done!')
    cmds.showWindow()

#END FUNCTIONS DEFINITION

#BEGIN CREATE WINDOW
cmds.window(title='Rename Object')
cmds.columnLayout(adj=1)
cmds.text(label= 'Insert Name', w=300, h=30)
cmds.separator()
txt_field = cmds.textField ('txtName') 
cmds.button(label='Renname', width=300, c=renameObject)
   
cmds.showWindow()
#END CREATE WINDOW




