#Important
Some of these files work assuming that you have your data to train the model stored in CSV files in a directory stored in the python variable
"INPUT_DATA_DIR" and you also have to change:

tempInput = np.array(frame[["Voltage(V)", "Current(A)", "Temperature(C)", "Previous SOC(%)"]])# so you init input here somehow
tempOutput = np.array(frame[["SOC(%)"]])# so you init output here 

The labels specified in these varibales must be the same as those at the top of each CSV file.
