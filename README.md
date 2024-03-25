# DonkeyCar-SOC
Files for SOC estimation of DonkeyCar batteries Spring 2023

In order to run the files on one of the DonkeyCars in the Tea lab you must have certain libraries downloaded. The main libraries are Spidev and Jetson.GPIO and a custom library called CustomTimer.

### Spidev 
In order to have SPI work on the Jetson, you must first set up the default pin usage setting to spi and not GPIO. This is done by following this page: https://jetsonhacks.com/2020/05/04/spi-on-jetson-using-jetson-io/

You type "sudo /opt/nvidia/jetson-io/jetson-io.py" in the terminal and navigate through the menu and turn SPI1 on. 

After this you need to install Spidev by typing "pip install spidev" in the terminal and you can find info on Spidev using: https://pypi.org/project/spidev/

### Jetson.GPIO
In order to install jetson.GPIO, you need to tpye "sudo pip install Jetson.GPIO" in the terminal and you can find information on it at: https://github.com/NVIDIA/jetson-gpio/blob/master/README.md

### CustomTimer
CustomTimer is a class that was taken from Python Assets in "Executing Code Every Certain Time" and adjusted to work more like a library would. In order to use it, you have to have "threading" pip installed in python if not already, and just make sure that CustomTimer.py is in the same file directory as the file that is calling it. You import it into the file in the same directory using "import CustomTimer as CT". You initialize it with "Timer1 = CT.CustomTimer(1, readvalues)" where 1 is the frequency that the funciton readvalues is called. To start or stop the timer you use "Timer1.start()" or "Timer1.stop()"
