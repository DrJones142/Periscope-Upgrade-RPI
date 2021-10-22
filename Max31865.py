import time
import board
import digitalio
import adafruit_max31865


# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=4)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
# sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=2)

# Main loop to print the temperature every second.
while True:
    # Read temperature.
    temp = sensor.temperature
    tempF = temp*9/5 +32 #convert to Farheneit 
    # Print the value.
    print("Temperature: {0:0.3f}F".format(tempF),"{0:0.3f}C".format(temp))
    # Delay for a second.
    time.sleep(1.0)
