import Jetson.GPIO as GPIO 
import time

# DO NOT USE CHANNELS 19, 21, 23, 24, 26. THEY ARE NOW CONFIGURED TO SPI.

GPIO.setmode(GPIO.BOARD) # CORRESPONDS TO THE NANO PINOUT NUMBERS ON THE PHYSICAL BOARD 

input_channel = 12
output_channel = 18

GPIO.setup(input_channel, GPIO.IN)
GPIO.setup(output_channel, GPIO.OUT)

GPIO.output(output_channel, GPIO.HIGH)
time.sleep(5)
GPIO.output(output_channel, GPIO.LOW)
time.sleep(5)
GPIO.output(output_channel, GPIO.HIGH)
time.sleep(5)

GPIO.cleanup()
