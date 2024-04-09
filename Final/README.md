# Final Files
These files are the final files that generate data, train the nueral network, and use the newural network to predict SOC.

### GenerateData File
This file when connected correctly to the circuit board and SOC gauge chip. The correct connections are explained in the google doc. You have to have the SOC gauge chip connected to calculate the corresponding SOC for training data. This file will read the Voltage(V), Current(A), Temperature(F), Previous SOC(%), and Current SOC(%) every 1 second. You type q and press enter to stop code. It will output to a CSV file that is named baised off of the time it was started and will store all the data into a csv file. You then need to move each CSV file into its own file for the training file to be able to correctly call the data up to train. We used this file in this order: we opened two command terminal windows each in the python virtual enviorment, navigated to the run.py file to run the car and move the wheels in one terminal and navigated to this file in the other terminal, connected the battery, started this file in its own terminal window, switched the switch to on, and then started the run.py file. We typed q and pressed enter when it hit 0%.

This file has a lot going on, it uses spi to communicate with the ADC(ADC124S101) using spidev, uses the Jetson.GPIO interrupts to listen for the SOC gauge chip(LTC4150). A lot of the logic and calculations are baised off of how the hardware works.

### Train.py
This file is used to train the neural network to predict SOC %. It will use Keras, pandas, skilearn StandardScaler. It will open every CSV file in the file directory stored in the variable INPUT_DATA_DIR and store data from each file into one numpy array to be used. You need to change INPUT_DATA_DIR to correspond to the file that the training data is stored.

### Predict.py
