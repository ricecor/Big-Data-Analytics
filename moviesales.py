#Pandas library used to import the csv file and format it for the script
import numpy as np
import pandas as pd
dataFile = pd.read_csv (r'/Users/coreyrice/Desktop/Datamining/HighestGrossers.csv')

#Ignoring Chars in the string
dataFile['TOTAL FOR YEAR'] = dataFile['TOTAL FOR YEAR'].replace('\$|,','', regex=True)
dataFile['TOTAL FOR YEAR'] = pd.to_numeric(dataFile['TOTAL FOR YEAR'])

dataFile['TOTAL IN 2019 DOLLARS'] = dataFile['TOTAL IN 2019 DOLLARS'].replace('\$|,','', regex=True)
dataFile['TOTAL IN 2019 DOLLARS'] = pd.to_numeric(dataFile['TOTAL IN 2019 DOLLARS'])

dataFile['TICKETS SOLD'] = dataFile['TICKETS SOLD'].replace('\$|,','', regex=True)
dataFile['TICKETS SOLD'] = pd.to_numeric(dataFile['TICKETS SOLD'])

#IQR
tYQ3, tYQ1 = np.percentile(dataFile['TOTAL FOR YEAR'], [75, 25])
tYIQR = tYQ3 - tYQ1

tDQ3, tDQ1 = np.percentile(dataFile['TOTAL IN 2019 DOLLARS'], [75, 25])
tDIQR = tDQ3 - tDQ1

tiSQ3, tiSQ1 = np.percentile(dataFile['TICKETS SOLD'], [75, 25])
tiSIQR = tiSQ3 - tiSQ1

# Mean Median Mode for Total that year
tYMean = dataFile['TOTAL FOR YEAR'].mean()
tYMedian = dataFile['TOTAL FOR YEAR'].median()
tYMode = dataFile['TOTAL FOR YEAR'].mode()

#For Total in 2019 Dollars
tDMean = dataFile['TOTAL IN 2019 DOLLARS'].mean()
tDMedian = dataFile['TOTAL IN 2019 DOLLARS'].median()
tDMode = dataFile['TOTAL IN 2019 DOLLARS'].mode()

#For Tickets Sold
tiSMean = dataFile['TICKETS SOLD'].mean()
tiSMedian = dataFile['TICKETS SOLD'].median()
tiSMode = dataFile['TICKETS SOLD'].mode()

#Print for all data points

print('Mean Total that Year: ' + str(tYMean))
print('Median Total that Year: ' + str(tYMedian))
print('Mode Total that Year: ' + str(tYMode)) 
print('Mean Total in 2019 Dollars: ' + str(tDMean))
print('Median Total in 2019 Dollars: ' + str(tDMedian))
print('Mode Total in 2019 Dollars: ' + str(tDMode))
print('Mean Tickets Sold: ' + str(tiSMean))
print('Median Tickets Sold: ' + str(tiSMedian))
print('Mode Tickets Sold: ' + str(tiSMode))
print('IQR for Total that Year: ' + str(tYIQR))
print('IQR for Total in 2019 Dollars: ' + str(tDIQR))
print('IQR for Tickets Sold: ' + str(tiSIQR))
print('Q1 for Total that Year: ' + str(tYQ1))
print('Q1 for Total in 2019 Dollars: ' + str(tDQ1))
print('Q1 for Ticket Sales: ' + str(tiSQ1))
print('Q3 for Total that Year: ' + str(tYQ3))
print('Q3 for Total in 2019 Dollars: ' + str(tDQ3))
print('Q3 for Ticket Sales: ' + str(tiSQ3))