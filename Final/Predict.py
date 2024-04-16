import time
import csv
import numpy as np
import spidev #Allows SPI
import Jetson.GPIO as GPIO #Allows interrupts and GPIO functions
import CustomTimer as CT #A custom made timer adjusted from Python Assets in "Executing Code Every Certain Time". You define a function that you want to be repeated, and then create a CustomTimer object with the input CustomTimer(interval speed in seconds, function to be repeated).You must have the file CustomTimer in the same depository as the file youre calling it from.
from keras.models import Sequential
from keras.layers import Dense
from keras.saving import load_model
from joblib import dump, load

def readvalues(): #Repeat this function every 1 second
	global adc1, adc2, adc3, volt, curr, temp1, SOC, previous_SOC, temp

	adc1 = spi.xfer([in2_add, 0])
	adc2 = spi.xfer([in3_add, 0])
	adc3 = spi.xfer([in1_add, 0])
	
	temp1 = int.from_bytes(adc1, byteorder = 'big')
	temp = (temp1*converstion*100) -50
	temp = (temp*1.8)+32
	temp = round(temp,2)
	curr = int.from_bytes(adc2, byteorder = 'big')
	curr = ((curr * converstion) - 0.505) * curr_factor
	curr = round(curr,2)
	volt = int.from_bytes(adc3, byteorder = 'big')
	volt = volt * converstion * volt_factor
	volt = round(volt,2)

	
	previous_SOC = SOC
	SOC = beginning_SOC - count * SOC_factor
	SOC = SOC / beginning_SOC * 100
	SOC = round(SOC, 2)
	

	row = np.array([[volt, curr, temp, previous_SOC, SOC, InReg, wcount]])

	prediction = model.predict(row)
	actualpred = y_fit.inverse_transform(prediction)

	print(f"V = {str(volt)}, I = {str(curr)}, T = {str(temp)}, SOC = {str(actualpred)}%\n, W should be {np.round(actualpred, 0)}")


def callback_fn(tmp): #This function will be called when the CC_channel Pin dorps low(0V)
	global count
	count = count + 1 



#SPI INITIALIZATION---------------------------------------------------------------------------------------------
spi = spidev.SpiDev() #Initialize Spi channel to output on spi0(if looking at pinout, spi1 if using jetson-io) channel > Pin 19 is MISO, Pin 20 is MOSI, Pin 21 is SCK, and Pin 26 is CS. 
bus=0
device=1
spi.open(bus,device)
spi.max_speed_hz = 100000 #100kHz baude rate


#TIMER INITIALIZATION---------------------------------------------------------------------------------------------
in1_add = 0<<3 #All are binary numbers that will be sent to the ADC to specify we want to read channel 1/2/3. Need 1<<11 but SPI sends it is 8 bit sections so split MSB to 1<<3 and LSB to 0 > 00001000 0000000
in2_add = 1<<3
in3_add = 2<<3
adc1 = 0
adc2 = 0 
adc3 = 0 
volt = 0
curr = 0
temp = 0
converstion = 3.3/4096
volt_factor = (67.8 + 32.9)/32.9
curr_factor = 1/(50*0.0025)

Timer1 = CT.CustomTimer(2, readvalues) #Initializes a timer that repeats a function every 1 second while letting the rest of the code run



#INTERRUPT INITIALIZATION---------------------------------------------------------------------------------------------
GPIO.setmode(GPIO.BOARD) #Corresponds to the nano pinout numbers on the physical board 
CC_channel = 12 #Set Pin 12 to be the channel connecting to CC
GPIO.setup(CC_channel, GPIO.IN) 
count = 0 #This variable will be incremented everytime the CC_channel goes low

beginning_SOC = 1200
SOC = 0
previous_SOC = SOC
SOC_factor = 1.707

#GPIO.add_event_detect(CC_channel, GPIO.FALLING, callback=callback_fn)

#NN INITIALIZATION
model = load_model('SOC_NN_Model.keras')
x_fit = load(x_fit_obj.bin)
y_fit = load(y_fit_obj.bin)

print("Enter any key to start!\nOnce started, enter 'q' to end code.")
input()
print("Starting")
InReg = 1
#Start Timer
Timer1.start()


while(True):
	temp = input()
	if temp == "q":
		print("Exited")
		Timer1.stop()
		time.sleep(1)
		spi.close()
		GPIO.cleanup()
		break
