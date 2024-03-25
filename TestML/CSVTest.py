import time
import csv

#Create current time in format of month_day_year_hour_minute
curTime = time.strftime("%m_%d_%y_%H_%M", time.localtime())

# name of csv file SOC_Data_month_day_year_hour_minute
filename = "SOC_Data_" + curTime + ".csv"
print("Filename is: " + filename)

# field names
fields = ['Voltage(V)', 'Current(A)', 'Temperature(C)', 'Previous SOC(%)', 'SOC(%)']
# data rows of csv file

#Create rows of data
V = 1
C = 2
T = 3
PSOC = 4
SOC = 5

V1 = 6
C1 = 7
T1 = 8
PSOC = 9
SOC1 = 10

row = [V,C,T,PSOC, SOC]
row1 = [V1,C1,T1,PSOC, SOC1]

# writing to csv file
with open(filename, 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerow(row)
    csvwriter.writerow(row1)
