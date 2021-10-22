# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.



from board import SCL, SDA
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)


# Set the PWM frequency to 60hz.
pca.frequency = 1000

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.



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

time.sleep(5)

led_channel1.duty_cycle = 0
led_channel2.duty_cycle = 0
led_channel3.duty_cycle = 0
led_channel4.duty_cycle = 0
led_channel5.duty_cycle = 0


