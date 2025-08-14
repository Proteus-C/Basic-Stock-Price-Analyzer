import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Opens and reads the JSON file containing stock prices
with open("StockPrice.json", 'r') as f:
    #Loads Json file data into Pandas DataFrame
    data = pd.read_json(f)

#Makes sure the data is in the correct format / datatype
data['Date'] = pd.to_datetime(data['Date'])
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
data['Price'].replace(0, np.nan, inplace=True)

#Fills in missing data with calculated prices from interpolate
data['Price'].interpolate(inplace=True)
data['Price'] = data['Price'].round(2)



#Converts Pandas 'Price' column to a numpy array
priceArray = data['Price'].to_numpy()

#gets the Day to Day percentage difference
percentDTD = []
for i in range(0, len(priceArray) - 1):
    calc = (priceArray[i+1] / priceArray[i]) - 1
    percentDTD.append(calc * 100)

#Gets the average price of the stock
average = np.mean(priceArray)

#Gets the overall standard derivations
derivationAvg = np.std(priceArray, ddof=1)

'''
print(f"{data} \n")
print(f"{percentDTD} \n")
print(f"{average} \n")
print(f"{derivationAvg} \n")
'''
