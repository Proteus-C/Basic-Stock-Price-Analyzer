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
data['Price'] = data['Price'].replace(0, np.nan)

#Fills in missing data with calculated prices from interpolate
data['Price'] = data['Price'].interpolate()
data['Price'] = data['Price'].round(2)



#Converts Pandas 'Price' column to a numpy array
priceArray = data['Price'].to_numpy()

#gets the Day to Day percentage difference
percentDTD = []
for i in range(0, len(priceArray) - 1):
    calc = (priceArray[i+1] / priceArray[i]) - 1
    percentDTD.append(calc * 100)
DTD = np.array(percentDTD)
DTD = DTD.round(2)

#Gets the average price of the stock
average = np.mean(priceArray)

#Gets the overall standard deviation
deviation = np.std(priceArray, ddof=1)
upperDev = average + deviation
lowerDev = average - deviation


plt.figure(figsize=(11, 6))
plt.plot(data["Date"], data["Price"])
#plt.fill_between(data["Date"], data["Price"], upperDev)        #Need to implement upper deviation fill
#plt.fill_between(data["Date"], data["Price"], lowerDev)        #Need to implement lower deviation fill 
plt.title("Stock Price Over Time")
plt.xlabel("Date")
plt.xticks(data["Date"][::1], rotation=45)  # Show every date at an angle
for i in range(0, len(data['Date']) - 1):
    plt.text(data['Date'].iloc[i + 1], 211.50, DTD[i], horizontalalignment = 'right', verticalalignment='top')
plt.ylabel("Price")
plt.grid(True)
plt.show()

