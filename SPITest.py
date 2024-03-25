import spidev
import time


spi = spidev.SpiDev()
bus=0
device=1
spi.open(bus,device)
spi.max_speed_hz = 100000

a = 1<<3

'''
print(a<<8)
spi.writebytes([a,0])
'''


for i in range(100):
	print(i)
	spi.writebytes([i])
	time.sleep(0.1)
print("Made this far")

spi.close()
