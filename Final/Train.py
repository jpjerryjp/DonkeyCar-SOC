# first neural network with keras tutorial
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.model_selection import train_test_split
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import matplotlib as mpl 
import numpy as np
import pandas as pd
from pandas import read_csv
from os import walk
from joblib import dump, load

INPUT_DATA_DIR = "C://Users//david//Desktop//UF Senior 2023-2024//EEL4924C//ML//5th Model//TrainingData//"

files = []

for (dirpath, dirnames, filenames) in walk(INPUT_DATA_DIR):
    files.extend(filenames)
    break

def generate_data(files):

    for file in files:
        frame = pd.read_csv(INPUT_DATA_DIR + file)
        tempInput = np.array(frame[["Voltage(V)", "Current(A)", "Temperature(C)", "InReq","SOC(%)"]]) # so you init input here somehow , "Previous SOC(%)"
        tempOutput = np.array(frame[["wcount"]]) # so you init output here
        try:
            input
        except NameError:
            input = tempInput
            output = tempOutput
            print(np.size(input))
            print(np.size(output)) 
        else:  
            input = np.concatenate((input, tempInput))
            output = np.concatenate((output, tempOutput))

    print(np.size(input))
    print(np.size(output))    
    return input, output
X, y = generate_data(files)

# Standardize X/y data set
x_standardize = StandardScaler()
x_fit = x_standardize.fit(X)
x_transform = x_fit.transform(X)
y_standardize = StandardScaler()
y_fit = y_standardize.fit(y.reshape(len(y),1))
y_transform = y_fit.transform(y.reshape(len(y),1))
dump(x_fit, 'x_fit_obj.bin', compress=True)
dump(y_fit, 'y_fit_obj.bin', compress=True)

# Manual split
seed = 7
np.random.seed(seed)
X_train, X_test, y_train, y_test = train_test_split(x_transform, y_transform, test_size=0.20, random_state=seed)

# Define the keras model
model = Sequential()
model.add(Dense(8, input_shape=(5,), activation='elu'))
model.add(Dense(6, activation='elu'))
model.add(Dense(3, activation='elu'))
model.add(Dense(1, activation='linear'))
opt = SGD(learning_rate = 0.01, momentum = 0.9)

# Compile the keras model
model.compile(loss='mean_squared_error', optimizer='adam')

# %%
history = model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=125, batch_size=15)
model.save('SOC_NN_Model.keras')
# Evaluate the model
train_mse = model.evaluate(X_train, y_train, verbose=0)
test_mse = model.evaluate(X_test, y_test, verbose=0)
print('Train Loss: %.3f, Test Loss: %.3f' % (train_mse, test_mse))

# Plot loss during training
plt.title('Loss / Mean Squared Error')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

temp2 = X
standinput2 = x_fit.transform(temp2)
prediction2 = model.predict(standinput2)
actualpred2 = y_fit.inverse_transform(prediction2)

for i in range (0,750,10):
    print("Expected Output=%s, Predicted Output=%s" % (y[i], actualpred2[i]))

# %%
plt.title('Predicted Output')
plt.plot(np.round(actualpred2, 0), 'r', label = 'Prediction')
plt.plot(y, marker = '.', label = 'Actual')
plt.ylabel('PWM Temrinal Input', size = 10)
plt.xlabel('Data Step', size = 10)
plt.legend(fontsize = 10)
plt.show()