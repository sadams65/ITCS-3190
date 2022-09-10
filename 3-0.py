# %% [markdown]
# # Configuring pandas

# %% [markdown]
# ### Documentation - https://pandas.pydata.org/docs/reference/index.html

# %%
# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)
    
# bring in matplotlib for graphics
import matplotlib.pyplot as plt
%matplotlib inline

# %% [markdown]
# # The pandas Series
# #### A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type. Read the documentation and create a series that contains 4 items. After that finish the following given cells.

# %%
# create a four item Series
new1 = pd.Series([1, 2, 3, 4])
new1

# %%
# get value at label 1
new1[1]

# %%
# Write a snippet of code that will return a Series with the row with labels 1 and 3
new1[[1,3]]

# %%
# create the same series but this time using an explicit index
new2 = new1 = pd.Series([1, 2, 3, 4])


# %%
# look up items the series having index at first and index at last position
new2[0:3]
new2

# %%
# get only the index of the Series
new2.index

# %%
# create a Series who's index is a series of dates
# https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
# between the two specified dates (inclusive)
# Dates: September 5, 2022 to September 11, 2022
new3 = pd.date_range('09/05/2022', '09/12/2022')
new3

# %%
# create a Series with values (representing temperatures) for each date in the index
# You can give them hardcoded values for now [80, 82, 85, 90, 83, 87, 80, 78]
# You can call this series clt_temp
clt_temp =pd.Series([80, 82, 85, 90, 83, 87, 80, 100], index = new3)
clt_temp

# %%
# what's the temperation for September 9?
clt_temp[4]

# %%
# create a second series of values using the same index
# You can give them hardcoded values for now [70, 75, 69, 83, 79, 77, 74, 79]
# You can call this series nycTemp
nyc_Temp = pd.Series([70, 75, 69, 83, 79, 77, 74, 100], index = new3)
nyc_Temp

# %%
# the series clt_temp and nyc_temp are aligned by their index values
# calculates the difference by those matching labels
difference = clt_temp - nyc_Temp
difference

# %%
# Write the code to find the temperature difference on September 8?
difference[3]

# %%
# Write code to find an average difference of temperature between the 2 cities?
difference.mean()

# %% [markdown]
# # The pandas DataFrame

# %%
# create a DataFrame from the two series objects clt_temp and nyc_temp
# and give them column names
temps_df = pd.DataFrame(
             {'Charlotte': clt_temp, 
              'NYC': nyc_Temp})
temps_df

# %%
# get the column with the name Charlotte
temps_df['Charlotte']

# %%
# likewise we can get just the NYC column
temps_df['NYC']

# %%
# return both columns in a different order

# %%
# retrieve the Charlotte column through PROPERTY SYNTAX
temps_df

# %%
# calculate the temperature difference between the two cities using the dataframe
temps_df.Charlotte - temps_df.NYC 

# %%
# add a column to temp_df which contains the difference in temps you can call the column Difference
temps_df['difference'] = temps_df['Charlotte'] - temps_df.NYC 
temps_df

# %%
# get the columns of the dataframe, which is also an Index object
temps_df.columns

# %%
# slice the temp differences column for the rows at 
# location 1 through 4 (as though it is an array)
temps_df['difference'][1:5]

# %%
# get the row at array position 1
temps_df.iloc[1] # you pass in a number where as loc is a specific set number

# %%


# %%
# the names of the columns have become the index
# they have been 'pivoted'
# retrieve a random row of your choice by index label using .loc
temps_df.loc[['2022-09-07']]

# %%
# get the values in the Differences column in tows 1, 3 and 5
# using 0-based location
temps_df.iloc[[1,3,5]]['difference']

# %%
# which values in the Missoula column are > 82?
temps_df.Charlotte > 82

# %%
# return the rows where the temps for Missoula > 82
temps_df[temps_df.Charlotte > 82]
temps_df.describe().loc['std']

# %% [markdown]
# # Loading data from a CSV file into a DataFrame

# %%
# read the contents of the file activity3_0.csv into a DataFrame. Call the dataframe df

# %%
# Print the contents of the date column

# %%
# Get the first value in the date column

# %%
# Write the code to get the type of the Date

# %%
# read the data and tell pandas the date column should be a date in the resulting DataFrame
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

# %%
# verify the type now is date
# in pandas, this is actually a Timestamp

# %%
# unfortunately the index is numeric which makes accessing data by date more complicated
# read in again, now specity the data column as being the index of the resulting DataFrame

# %%
# Verify that the index is now a DatetimeIndex by calling df.index

# %% [markdown]
# # Visualization

# %%
# plots the values in the Close column
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html

# %% [markdown]
# # Thats it for today :D Good job!!!!
# 
# #### Submit this notebook on canvas and you will be graded for correctness. Make sure that you are not cutting corners or shortcuts 


