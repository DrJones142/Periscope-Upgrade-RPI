# import everything from tkinter module
from tkinter import *   

 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('400x400')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

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

#cretes sliders (PWM gen)
PopUpSlider1 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
PopUpSlider2 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
PopUpSlider3 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
PopUpSlider4 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
# Set the position of button on the top of window.  


#creates sliders for LED brightness
PopUpLEDSlider1 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
PopUpLEDSlider2 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
PopUpLEDSlider3 = Scale(root,from_=0, to=255, orient=HORIZONTAL)
PopUpLEDSlider4 = Scale(root,from_=0, to=255, orient=HORIZONTAL)

PopUp1.grid(row=0,column=0)   
PopUpSlider1.grid(row=0,column=1)
PopUpLEDSlider1.grid(row=0,column=2)

PopUp2.grid(row=1,column=0)
PopUpSlider2.grid(row=1,column=1)
PopUpLEDSlider2.grid(row=1,column=2)

PopUp3.grid(row=2,column=0)
PopUpSlider3.grid(row=2,column=1)
PopUpLEDSlider3.grid(row=2,column=2)

PopUp4.grid(row=3,column=0)
PopUpSlider4.grid(row=3,column=1)
PopUpLEDSlider4.grid(row=3,column=2)

root.mainloop()