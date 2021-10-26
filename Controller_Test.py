
from board import SCL, SDA 
import busio
import time
import digitalio

from adafruit_mcp230xx.mcp23017 import MCP23017
from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)
mcp = MCP23017(i2c_bus)  # MCP23017

pin0 = mcp.get_pin(8)
pin1 = mcp.get_pin(9)
pin2 = mcp.get_pin(10)
pin3 = mcp.get_pin(11)

pin4 = mcp.get_pin(12)   #pins for relay
pin5 = mcp.get_pin(13)
pin6 = mcp.get_pin(14)
pin7 = mcp.get_pin(15)

pin0.switch_to_output(value=False)
pin1.switch_to_output(value=False)
pin2.switch_to_output(value=False)
pin3.switch_to_output(value=False)

pin4.switch_to_output(value=False)
pin5.switch_to_output(value=False)
pin6.switch_to_output(value=False)
pin7.switch_to_output(value=False)


pca.frequency = 1000

led_channel1 = pca.channels[0]

led_channel1.duty_cycle = 0xffff

led_channel2 = pca.channels[1]

led_channel2.duty_cycle = 0xffff

led_channel3 = pca.channels[2]

led_channel3.duty_cycle = 0xffff

led_channel4 = pca.channels[3]

led_channel4.duty_cycle = 0xffff

led_channel5 = pca.channels[4]
led_channel5.duty_cycle = 0x7fff

led_channel6 = pca.channels[5]
led_channel6.duty_cycle = 0x7fff

led_channel7 = pca.channels[6]
led_channel7.duty_cycle = 0x7fff

led_channel8 = pca.channels[7]
led_channel8.duty_cycle = 0x7fff

time.sleep(5)
pin0.value = True
pin1.value = True
pin2.value = True
pin3.value = True
time.sleep(5)
led_channel1.duty_cycle = 0
led_channel2.duty_cycle = 0
led_channel3.duty_cycle = 0
led_channel4.duty_cycle = 0
led_channel5.duty_cycle = 0
led_channel6.duty_cycle = 0
led_channel7.duty_cycle = 0
led_channel8.duty_cycle = 0

time.sleep(5)
pin4.value = True
time.sleep(1)
pin5.value = True
time.sleep(1)
pin6.value = True
time.sleep(1)
pin7.value = True
time.sleep(1)
pin4.value = False
time.sleep(1)
pin5.value = False
time.sleep(1)
pin6.value = False
time.sleep(1)
pin7.value = False

time.sleep(1)
pin4.value = True
pin5.value = True
pin6.value = True
pin7.value = True

time.sleep(0.5)
pin4.value = False
pin5.value = False
pin6.value = False
pin7.value = False