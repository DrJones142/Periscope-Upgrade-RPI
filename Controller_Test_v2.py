from board import SCL, SDA 
import busio
import time
import digitalio

from adafruit_mcp230xx.mcp23017 import MCP23017
from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)
mcp = MCP23017(i2c_bus)  # MCP23017

def raisePopUp(PopUpNum):
    if PopUpNum == 1:
        pin0.value = True
    elif PopUpNum == 2:
        pin1.value = True
    elif PopUpNum == 3:
        pin2.value = True
    elif PopUpNum == 4:
        pin3.value = True
    else:
        print("Invalid")

def lowerPopUp(PopUpNum):
    if PopUpNum == 1:
        pin0.value = False
    elif PopUpNum == 2:
        pin1.value = False
    elif PopUpNum == 3:
        pin2.value = False
    elif PopUpNum == 4:
        pin3.value = False
    else:
        print("Invalid")

def setPWMValue(channel,dutyCycle):
    dutyCycle_adjusted = dutyCycle*256
    pca.channels[channel].duty_cycle = dutyCycle_adjusted

pin0 = mcp.get_pin(8)
pin1 = mcp.get_pin(9)
pin2 = mcp.get_pin(10)
pin3 = mcp.get_pin(11)
pin0.switch_to_output(value=False)
pin1.switch_to_output(value=False)
pin2.switch_to_output(value=False)
pin3.switch_to_output(value=False)

pca.frequency = 1000

# raisePopUp(2)
# setPWMValue(5,255)
# setPWMValue(6,255)
# time.sleep(5)
# lowerPopUp(2)
# time.sleep(5)
# setPWMValue(5,0)
# setPWMValue(6,0)

led_channel1 = pca.channels[0]

led_channel1.duty_cycle = 0xffff

led_channel2 = pca.channels[1]

led_channel2.duty_cycle = 0xffff

led_channel3 = pca.channels[2]

led_channel3.duty_cycle = 0xffff

led_channel4 = pca.channels[3]

led_channel4.duty_cycle = 0xffff

led_channel5 = pca.channels[4]
led_channel5.duty_cycle = 0

led_channel6 = pca.channels[5]
led_channel6.duty_cycle = 0

led_channel7 = pca.channels[6]
led_channel7.duty_cycle = 0

led_channel8 = pca.channels[7]
led_channel8.duty_cycle = 0


# time.sleep(5)
# pin0.value = True
# pin1.value = True
# pin2.value = True
# pin3.value = True
# time.sleep(5)
# led_channel1.duty_cycle = 0
# led_channel2.duty_cycle = 0
# led_channel3.duty_cycle = 0
# led_channel4.duty_cycle = 0
# led_channel5.duty_cycle = 0
# led_channel6.duty_cycle = 0
# led_channel7.duty_cycle = 0
# led_channel8.duty_cycle = 0