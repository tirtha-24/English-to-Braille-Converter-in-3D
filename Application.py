import tkinter
from tkinter import *
import os

# e.g. blenderLocation = "C:\\Users\\User_name\\Desktop\\Folder_name\\Blender Foundation\\Blender"
blenderLocation = ""

# window
w = tkinter.Tk()
w.title("3D Braille Printer")
w.geometry("300x135")

# function to run when input text is ready
def submitInput ():
    os.chdir(blenderLocation)
   
    os.system("blender --b output.blend --python Blender3D.py -- " + inEntry.get())
    clearButton['state'] = NORMAL
    inButton['state'] = DISABLED

def clearFile ():
    os.chdir(blenderLocation)
    os.system("blender --b output.blend --python Clear3D.py")
    clearButton['state'] = DISABLED
    inButton['state'] = NORMAL

# label requesting input
inLabel = Label (w, text="Enter text to convert to braille:")

# text input field
inEntry = Entry (w)

# submit button for when input text is ready
inButton = Button (w, text="Convert", command=submitInput)

# label to indicate output area
clearLabel = Label (w, text="Clear .blend file:")

# button for user to retrieve processed blender file
clearButton = Button (w, text="Clear", state=DISABLED, command=clearFile)

inLabel.pack()
inEntry.pack()
inButton.pack()
clearLabel.pack()
clearButton.pack()
w.mainloop()
