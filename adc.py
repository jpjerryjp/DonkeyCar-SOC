import spidev
import time
import CustomTimer as CT

spi = spidev.SpiDev()
bus=0
device=1
spi.open(bus,device)
spi.max_speed_hz = 100000

in1_add = 0<<3
in2_add = 1<<3
in3_add = 2<<3
adc1 = 0
adc2 = 0 
adc3 = 0 
volt1 = 0
volt2 = 0
volt3 = 0

def readvalues():
	global adc1, adc2, adc3
	spi.writebytes([in1_add, 0])
	adc1 = spi.readbytes(2)
	time.sleep(0.1)
	spi.writebytes([in2_add,0])
	adc2 = spi.readbytes(2)
	time.sleep(0.1)
	spi.writebytes([in3_add,0])
	adc3 = spi.readbytes(2)
	time.sleep(0.1)

	volt1 = int.from_bytes(bytes=adc1, byteorder = 'big')
	volt2 = int.from_bytes(bytes=adc2, byteorder = 'big')
	volt3 = int.from_bytes(bytes=adc3, byteorder = 'big')
	print(f"Volt Channel 1: {volt1*3.3/4096}")
	print(f"Volt Channel 2: {volt2*3.3/4096}")
	print(f"Volt Channel 3: {volt3*3.3/4096}")

Timer1 = CT.CustomTimer(1, readvalues)
Timer1.start()

while (True):
	if input() == "q":
		break
Timer1.stop()
spi.close()
