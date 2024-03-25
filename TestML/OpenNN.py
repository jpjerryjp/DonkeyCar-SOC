import pandas as pd
import numpy as np
from os import walk
from keras.models import Sequential
from keras.layers import Dense
from keras.saving import load_model

INPUT_DATA_DIR = "C://Users//jerry//Documents//UF//2024 Spring//EEL4924C-EE Design 2//SOC Estimation Code//TestML//TestSOCData//"

files = []

for (dirpath, dirnames, filenames) in walk(INPUT_DATA_DIR):
    files.extend(filenames)
    break


def generate_data(files):

    for file in files:

        frame = pd.read_csv(INPUT_DATA_DIR + file)
        # here is your preprocessing

        tempInput = np.array(frame[["Voltage(V)", "Current(A)", "Temperature(C)", "Previous SOC(%)"]])# so you init input here somehow
        tempOutput = np.array(frame[["SOC(%)"]])# so you init output here
        #tempInput = np.array(frame[["a", "b", "c", "d", "e", "f", "g", "h"]])# so you init input here somehow
        #tempOutput = np.array(frame[["i"]])# so you init output here
        try:
            input
        except NameError:
            input = tempInput
            output = tempOutput
            print(input.shape)
            print(output.shape) 
        else:  
            input = np.concatenate((input, tempInput))
            output = np.concatenate((output, tempOutput))

    print(input.shape)
    print(output.shape)    
    return input, output
input, output = generate_data(files)


model = load_model('Test_SOC_model.keras')

predictions = model.predict(input)
for i in range(0,100,10):
    print(f"Predictions = {predictions[i,:]}, expected = {output[i,:]}")