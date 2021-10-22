# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('400x400')

def activatePopUp1():
    if PopUp1['text']=="Pop Up 1 Deactivated":
        PopUp1['text']="Pop Up 1 Activated"
    else:
        PopUp1['text']="Pop Up 1 Deactivated"

def activatePopUp2():
    if PopUp2['text']=="Pop Up 2 Deactivated":
        PopUp2['text']="Pop Up 2 Activated"
    else:
        PopUp2['text']="Pop Up 2 Deactivated"

def activatePopUp3():
    if PopUp3['text']=="Pop Up 3 Deactivated":
        PopUp3['text']="Pop Up 3 Activated"
    else:
        PopUp3['text']="Pop Up 3 Deactivated"


def activatePopUp4():
    if PopUp4['text']=="Pop Up 4 Deactivated":
        PopUp4['text']="Pop Up 4 Activated"
    else:
        PopUp4['text']="Pop Up 4 Deactivated"
# Create a Button
PopUp1 = Button(root, text = 'Pop Up 1 Deactivated', bd = '5',
                          command = activatePopUp1)
PopUp2 = Button(root, text = 'Pop Up 2 Deactivated', bd = '5',
                          command = activatePopUp2) 
PopUp3 = Button(root, text = 'Pop Up 3 Deactivated', bd = '5',
                          command = activatePopUp3)
PopUp4 = Button(root, text = 'Pop Up 4 Deactivated', bd = '5',
                          command = activatePopUp4)
# Set the position of button on the top of window.  


PopUp1.pack(side = 'top')   
PopUp2.pack(side = 'top')
PopUp3.pack(side = 'top')
PopUp4.pack(side = 'top') 
root.mainloop()