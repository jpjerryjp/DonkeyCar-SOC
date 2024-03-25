import time
import CustomTimer as CT #A custom made timer adjusted from Python Assets in "Executing Code Every Certain Time". You define a function 
#that you want to be repeated, and then create a CustomTimer object with the input CustomTimer(interval speed in seconds, function to be repeated). 
#You must have the file CustomTimer in the same depository as the file youre calling it from.

def timer():
        print("Testing...")

Timer1 = CT.CustomTimer(1, timer)
Timer1.start()
time.sleep(2)
Timer1.stop()