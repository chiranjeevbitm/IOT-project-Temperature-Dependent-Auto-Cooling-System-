# importing libraries

import RPi.GPIO as GPIO 
from time import sleep 

#importing the Adafruit library
import Adafruit_DHT


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# create an instance of the sensor type
sensor = Adafruit_DHT.AM2302

print (‘Getting data from the sensor’)

#humidity and temperature are 2 variables that store the values received from the sensor

humidity, temperature = Adafruit_DHT.read_retry(sensor,17)
print ('Temp={0:0.1f}*C humidity={1:0.1f}%'.format(temperature, humidity))

