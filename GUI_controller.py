# import everything from tkinter module
from tkinter import *   

from Controller_Test_v2 import *

# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('600x600')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

var = IntVar()

def activatePopUp1():
    if PopUp1['text']=="Pop Up 1 Deactivated":
        PopUp1['text']="Pop Up 1 Activated"
        raisePopUp(1)
    else:
        PopUp1['text']="Pop Up 1 Deactivated"
        lowerPopUp(1)

def activatePopUp2():
    if PopUp2['text']=="Pop Up 2 Deactivated":
        PopUp2['text']="Pop Up 2 Activated"
        raisePopUp(2)
    else:
        PopUp2['text']="Pop Up 2 Deactivated"
        lowerPopUp(2)

def activatePopUp3():
    if PopUp3['text']=="Pop Up 3 Deactivated":
        PopUp3['text']="Pop Up 3 Activated"
        raisePopUp(3)
    else:
        PopUp3['text']="Pop Up 3 Deactivated"
        lowerPopUp(3)

def activatePopUp4():
    if PopUp4['text']=="Pop Up 4 Deactivated":
        PopUp4['text']="Pop Up 4 Activated"
        raisePopUp(4)
    else:
        PopUp4['text']="Pop Up 4 Deactivated"
        lowerPopUp(4)

## functions for PWM Slider (speed)

def setPWMSlider1(Slider1_value):
    pwmValue = int(Slider1_value)
    setPWMValue(4,pwmValue)

def setPWMSlider2(Slider2_value):
    setPWMValue(5,int(Slider2_value))

def setPWMSlider3(Slider3_value):
    setPWMValue(6,int(Slider3_value))

def setPWMSlider4(Slider4_value):
    setPWMValue(7,int(Slider4_value))

## functions for PWM (brightness) 

def setPWMLEDSlider1(SliderLED1_value):
    pwmValue = int(SliderLED1_value)
    setPWMValue(0,pwmValue)

def setPWMLEDSlider2(SliderLED2_value):
    pwmValue = int(SliderLED2_value)
    setPWMValue(1,pwmValue)

def setPWMLEDSlider3(SliderLED3_value):
    pwmValue = int(SliderLED3_value)
    setPWMValue(2,pwmValue)

def setPWMLEDSlider4(SliderLED4_value):
    pwmValue = int(SliderLED4_value)
    setPWMValue(3,pwmValue)       

def RadioButtonSelect():
    print("You selected option " +str(var.get()))

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
PopUpSlider1 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMSlider1)
PopUpSlider2 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMSlider2)
PopUpSlider3 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMSlider3)
PopUpSlider4 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMSlider4)
# Set the position of button on the top of window.  


#creates sliders for LED brightness
PopUpLEDSlider1 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMLEDSlider1)
PopUpLEDSlider2 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMLEDSlider2)
PopUpLEDSlider3 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMLEDSlider3)
PopUpLEDSlider4 = Scale(root,from_=0, to=255, orient=HORIZONTAL,command=setPWMLEDSlider4)

#creates Radiobuttons for tip/tilts

MotorMikeA_EL = Radiobutton(root,text="A EL",variable=var,value=0,command=RadioButtonSelect)
MotorMikeA_AZ = Radiobutton(root,text="A AZ",variable=var,value=1,command=RadioButtonSelect)

MotorMikeB_EL = Radiobutton(root,text="B EL",variable=var,value=2,command=RadioButtonSelect)
MotorMikeB_AZ = Radiobutton(root,text="B AZ",variable=var,value=3,command=RadioButtonSelect)

MotorMikeC_EL = Radiobutton(root,text="C EL",variable=var,value=4,command=RadioButtonSelect)
MotorMikeC_AZ = Radiobutton(root,text="C AZ",variable=var,value=5,command=RadioButtonSelect)

MotorMikeD_EL = Radiobutton(root,text="D EL",variable=var,value=6,command=RadioButtonSelect)
MotorMikeD_AZ = Radiobutton(root,text="D AZ",variable=var,value=7,command=RadioButtonSelect)

MotorMikeB_Rotate45 = Radiobutton(root,text="B Rot 45 (EL)",variable=var,value=8,command=RadioButtonSelect)
MotorMikeB_Lock = Radiobutton(root,text="B Lock",variable=var,value=9,command=RadioButtonSelect)


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

MotorMikeA_EL.grid(row=4,column=0)
MotorMikeA_AZ.grid(row=4,column=1)

MotorMikeB_EL.grid(row=5,column=0)
MotorMikeB_AZ.grid(row=5,column=1)

MotorMikeC_EL.grid(row=6,column=0)
MotorMikeC_AZ.grid(row=6,column=1)

MotorMikeD_EL.grid(row=7,column=0)
MotorMikeD_AZ.grid(row=7,column=1)

MotorMikeB_Rotate45.grid(row=8,column=0)
MotorMikeB_Lock.grid(row=8,column=1)

root.mainloop()