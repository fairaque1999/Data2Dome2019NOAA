import pandas as pd

data = pd.read_csv('insert filepath here', sep='\s+', na_values=['*', '**', '***', '****', '*****', '******'])

select_cols = ['YR--MODAHRMN', 'DIR', 'SPD', 'GUS', 'TEMP', 'MAX', 'MIN']

data = data[select_cols]

name_conversion_dict = {'YR--MODAHRMN':'TIME', 'SPD':'SPEED', 'GUS':'GUST' }

data = data.rename(columns = name_conversion_dict)

#The function
def FahrToCelsius(temp_fahrenheit):
    converted_temp = (temp_fahrenheit-32)/1.8
    return converted_temp

#Create an empty column for the data   
col_name = 'Celsius'
data[col_name] = None

#Iterations
for idx, row in data.iterrows():
    #conversion
    celsius = FahrToCelsius(row['TEMP'])
    #adding the values to the Celsius Column
    data.loc[idx,col_name] = celsius

#Converting units of wind speed    
data['SPEED'] = data['SPEED']*0.44704
data['GUST'] = data['GUST']*0.44704

#We'll have to slice the values in the TIME column to make them hourly
#To do that we need to convert the type of the values in the column from int to str
data['TIME_str'] = data['TIME'].astype(str)

#Slicing the minute values from the TIME column
data['TIME_dh'] = data['TIME_str'].str.slice(start=0, stop=10)

#Now we slice and separate the hourly values into a new column and convert then to int
data['TIME_h'] = data['TIME_str'].str.slice(start=8, stop=10)
data['TIME_h'] = data['TIME_h'].astype(int) #Now we have a separate column for only the hour of the day

#Creating an empty dataframe
aggr_data = pd.DataFrame()

#Grouping the data based on day and hour attributes
grouped = data.groupby('TIME_dh')

#Creating a list of the columns we want to aggregate
mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP', 'Celsius', 'TIME_h']

#Iterating over the groups
for key, group in grouped:
    #Aggregate the data
    mean_values = group[mean_cols].mean()
    #Add the key (the datetime information) into the aggregated values
    mean_values['TIME_dh'] = key
    #Append the aggregated values into the dataframe
    aggr_data = aggr_data.append(mean_values, ignore_index=True)
    
#Now we're looking for outliers in our data to indicate any storms specifically any outlying value
    #so we're looking for SPEED values that are twic std away from the mean value

std_wind = aggr_data['SPEED'].std()
avg_wind = aggr_data['SPEED'].mean()

print('Std:',std_wind)
print('Mean:',avg_wind)

upper_threshold = avg_wind + (std_wind*2)
print('Upper threshold for outlier:', upper_threshold)

#Creating an empty column for outlier info
aggr_data['Outlier'] = None

#Iterating over the rows and testing for outliers
for idx, row in aggr_data.iterrows():
    if row['SPEED']>upper_threshold:
        aggr_data.loc[idx, 'Outlier'] = True
    else:
        aggr_data.loc[idx, 'Outlier'] = False
print(aggr_data)
storm = aggr_data.ix[aggr_data['Outlier'] == True]
print(storm)

