import pandas as pd
import numpy as np
from os import walk
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import normalize, StandardScaler
#INPUT_DATA_DIR = "C://Users//jerry//Documents//UF//2024 Spring//EEL4924C-EE Design 2//SOC Estimation Code//TestML//TestMLCSV//"
INPUT_DATA_DIR = "C://Users//jerry//Documents//UF//2024 Spring//EEL4924C-EE Design 2//SOC Estimation Code//TestML//TestSOCData//"

files = []

for (dirpath, dirnames, filenames) in walk(INPUT_DATA_DIR):
    files.extend(filenames)
    break

'''
frame = pd.read_csv(INPUT_DATA_DIR + files[0])
input = np.array(frame[["Voltage(V)", "Current(A)", "Temperature(C)", "Previous SOC(%)"]])# so you init input here somehow
output = np.ravel(frame[["SOC(%)"]])# so you init output here
'''

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

#print(f"input = {input}")
#print(f"output = {output}")

input_scaler = StandardScaler()
output_scaler = StandardScaler()
input_model = input_scaler.fit(input)
output_model = output_scaler.fit(output)
new_input = input_model.transform(input)
new_output = output_model.transform(output)
#print(f"new input = {new_input}")
#print(f"new ouput = {new_output}")

old_input = input_model.inverse_transform(new_input)
old_output = output_model.inverse_transform(new_output)
#print(f"old input = {old_input}")
#print(f"old ouput = {old_output}")




model = Sequential()
model.add(Dense(20, input_shape=(4,), activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='softplus'))
# compile the keras model
model.compile(loss='mean_squared_error', optimizer='adam')

# fit the keras model on the dataset
#model.fit(x = input, y = output, batch_size=10, 
#          epochs=100, verbose=1)
model.fit(x = input, y = output, batch_size=10, 
          validation_split = 0.10, epochs=100, verbose=1)

predictions = model.predict(input)
for i in range(0,100,10):
    print(f"Predictions = {predictions[i,:]}, expected = {output[i,:]}")

model.save('Test_SOC_model.keras')

'''
predictions = model.predict(new_input)
# summarize the first 5 cases

real_predicted = output_model.inverse_transform(predictions)

for i in range(0,100,10):
    print(f"Predictions = {predictions[i,:]}, expected = {new_output[i,:]}")

for i in range(0,100,10):
    print(f"Real Predictions = {real_predicted[i,:]}, Real expected = {old_output[i,:]}")
    '''