import time
import Jetson.GPIO as GPIO #Allows interrupts and GPIO functions
import CustomTimer as CT #A custom made timer adjusted from Python Assets in "Executing Code Every Certain Time". You define a function that you want to be repeated, and then create a CustomTimer object with the input CustomTimer(interval speed in seconds, function to be repeated).You must have the file CustomTimer in the same depository as the file youre calling it from.
import ctypes
import pylibi2c

# Open i2c device @/dev/i2c-0, addr 0x50.
i2c = pylibi2c.I2CDevice('/dev/i2c-0', 0x02, iaddr_bytes=0) 

# Set delay
i2c.delay = 10

# Set page_bytes
#i2c.page_bytes = 16

# Python3
#buf = bytes([1])
#buf = int.from_bytes(1,byteorder = 'big')
i = 0

def timer1Callback(): #Repeat this function every 1 second
	global i
	i = i + 1 
	buf = bytes([i])
	print(f"buf = {buf}")
	i2c.ioctl_write(0x0, buf)
	x = i2c.ioctl_read(0x0, 1)
	print(f"Read {x}")

Timer1 = CT.CustomTimer(2, timer1Callback) #Initializes a timer that repeats a function every 1 second while letting the rest of the code run
Timer1.start()

# Write data to i2c, buf must be read-only type
while(True):
	if input() == "q":
		Timer1.stop()
		break

'''
# Open i2c device @/dev/i2c-0, addr 0x50, 16bits internal address
i2c = pylibi2c.I2CDevice('/dev/i2c-0', 0x50, iaddr_bytes=2)

# Set delay
i2c.delay = 10

# Set page_bytes
i2c.page_bytes = 16

# Python3
buf = bytes(256)

# Write data to i2c, buf must be read-only type
size = i2c.write(0x0, buf)

# From i2c 0x0(internal address) read 256 bytes data, using ioctl_read.
data = i2c.ioctl_read(0x0, 256)
'''
