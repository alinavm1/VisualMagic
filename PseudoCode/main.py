# Import Maya Module

# Get All objects in Hierarchy

# Loop over all objects
    # Get ObjectType (i.e geometry, constraints etc)

    # Is Object Type Geometry?
        #Get Object Name
        #Set Object Name + Geometry Suffix of choice
    # Is Object Constratint?
        # Get Object Name
        # Add suffix to object name
        # Call maya function for settings object name to new name

from maya import cmds

# Get Selected Objects using
selected = cmds.ls(sl=True, long=True)

for object in selected:
    print(cmds.objectTYpe(object))

# Loop over all objects using for object in selected
    # Check if object is a curve objectType = cmds.objectType(object) 
        # GetCurvePositionInformation using cmds.pointOnCurve(curve, position=.5)
        # Get World Position = cmds.getAttr(infoNode + ".position")
        # Do something cool with this position


#ctrl+shift+p to open the command palette

# Load the maya commands library
from maya import cmds

# Create a new variable 'selection' 
# Store in it the currently selected objects
selection = cmds.ls(selection=True)

# If selection contains 0 lists
if len(selection) == 0:

    # Then get all objects in the outliner and assign to 'selection'
    # long=True : Gives us the full path to the object, so we can determine any parents.
    # dag=True : We will only get objects which are listed in the outliner, and none of the hidden objects inside of Maya.
    selection = cmds.ls(dag=True, long=True)

# Sort the list now stored in 'selection'
# Sort by length
# In reverse, giving us the longest path first
selection.sort(key=len, reberse=True)

# For each object now in the 'selection' variable
for obj in selection:

    # Split the path by "│" (pipe)
    # Store in a new variable 'shortName'
    shortName = obj.split  ("│")[-1] 

    # Lets create a new variable to store the relatives
    # We want to list the relatives, we only want the children, and we want the full path
    # If there are no relative, return an empty list (or[]), so that we always get a consistent object type output
    children = cmds.listRelatives(obj, children=True, fullPath=True) or []

    # If the length of the children is exactly 1 (remeber this is in a for loop)
    if len(children) == 1:

        # Then put the object at position 0 in the children list into a new variabel 'child'
        child = children[0]

        # Place the objecttype of the child variable in the variable 'objtype'
        objType = cmds.objectType(child)
        print(objType)
        if objType == "nurbsCurve":
            #cmds.pointOnCurve(obj)
            print("find point on curve")
    else:

            # Otherwise if the length of children is NOT 1 (so basically 0)
            # Put the object type of the object in the objectype variable
            objType = cmds.objectType(obj)
            print(objType)
            if objType == "nurbsCurve":
                #cmds.pointOnCurve(obj)
                print("find point on curve")


    # print the objtype variable









