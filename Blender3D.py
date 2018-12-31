import bpy
import sys
import os

argv = sys.argv
argv = argv[argv.index("--") + 1:]
dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

import EngToBraille

inpu = EngToBraille.translate(" ".join(argv))
def createBraille(my_bool,x,y):
    #create cube
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(x, y, 0.5), rotation=(1.57, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    
    bpy.ops.transform.resize(value=(0.25, 0.25, 0.125), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    if(my_bool):
        #add cylinder
        bpy.ops.mesh.primitive_cylinder_add(radius=0.125, depth=0.125, view_align=False, enter_editmode=False, location=(x, y, 0.625), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    
        
        


X = 0
Y = -8
letterCount = 0

createBraille(0,X,-9)
createBraille(0,X,-8.5)
createBraille(0,X+0.5,-9)
createBraille(0,X+0.5,-8.5)
createBraille(0,X+1,-9)
createBraille(0,X+1,-8.5)

for word in inpu:
  letterCount=0
  for letter in word:
    letterCount += 1
    for i in range(0,3):
        createBraille(letter[2*i],X,Y)
        createBraille(letter[2*i+1],X,Y+0.5)
        X += 0.5
    Y += 1
    X = 0
    if(letterCount==len(word)):
        createBraille(0,X,Y)
        createBraille(0,X,Y+0.5)
        createBraille(0,X+0.5,Y)
        createBraille(0,X+0.5,Y+0.5)
        createBraille(0,X+1,Y)
        createBraille(0,X+1,Y+0.5)
        Y+=1

  
bpy.ops.wm.save_as_mainfile()

