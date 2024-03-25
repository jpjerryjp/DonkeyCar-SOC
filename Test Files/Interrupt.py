import Jetson.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD) # CORRESPONDS TO THE NANO PINOUT NUMBERS ON THE PHYSICAL BOARD 

input_channel = 12
output_channel = 18
count = 0
a = 0.1707 
capacity = 0

GPIO.setup(input_channel, GPIO.IN)
GPIO.setup(output_channel, GPIO.OUT)

# define callback function
def callback_fn(tmp):
	global count
	count = count + 1 

# add rising edge detection
GPIO.add_event_detect(input_channel, GPIO.RISING, callback=callback_fn)

while (True):
	print("COUNT IS: " + str(count)) 
	time.sleep(2)
	capacity = count * a 
	print("CAPACITY IS: " + str(capacity))

GPIO.cleanup()
