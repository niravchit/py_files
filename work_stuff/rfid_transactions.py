import pandas as pd
import os
import datetime
import numpy as np 

#filepath for xls file
filepath = r'C:\Users\nirav.chitkara\Documents\Filtered Transactions.xls'

#helper function to load excel file into a dataframe. 
#filepath is argument, default value is defined filepath 
def load_df(fp = filepath):
    transactions = pd.read_excel(fp, na_values=['NA'])
    return transactions

#helper function to convert numpy datetime to time from epoch time in seconds
def convert_time(dt64):
    return (dt64 - np.datetime64('1970-01-01T00:00:00Z'))/np.timedelta64(1,'s')

#load transactions variable as dataframe from xls file
transactions = load_df()
#transactions.set_index(['Item#', 'Location'], inplace = True)

transactions['Epoch Date'] = pd.Series(map(convert_time, transactions['Date']))
transactions['Tdate'] = transactions['Date']
#print(transactions.head())

#print(transactions['Epoch Date'][4] - transactions['Epoch Date'][3])

# for item, new_trans in transactions.groupby(['Item#']):
#     #print(new_trans)
#     new_trans['Time Delta'] = new_trans['Tdate'].diff().dt.seconds.div(60, fill_value = 0)
#     #print(new_trans.loc[new_trans['Item#'] == '17CA0001C1E100'])
    


#transactions.sort(['Item#','Location'], inplace = True)
#transactions.sort_values(['Item#','Tdate'], ascending = True).groupby('Item#')
#new_transactions = transactions.groupby(['Item#'])['Epoch Date'].apply(lambda x: x.sort_values())

#transactions['Time Delta'] = transactions.groupby(['Item#'])['Tdate'].diff().dt.total_seconds()
#print(transactions.head(6))

#set new value Time Delta in dataframe
#sort values in data frame by item and then by the epoch date for each station transaction for an item in ascending order
#group them by item and then for the tdate field, calculate the difference between consecutive rows and convert to total seconds
#first row for each grouping considered start so no delta for it
transactions['Time Delta'] = transactions.sort_values(['Item#','Epoch Date'], ascending = True).groupby(['Item#'])['Tdate'].diff().dt.total_seconds()
print(transactions.head(30))
