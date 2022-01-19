import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import numpy as np
from sklearn import linear_model

data = pd.read_csv('data/covid.csv')
print(data.columns)

data['diff_deceased'] = data['deceased'].diff()
data['diff_swabs'] = data['swabs'].diff()
dates = data['date']
date_format = [pd.to_datetime(d) for d in dates]

variable = 'new_positives'
name = "New positive"
fig, ax = plt.subplots(figsize=(12, 5))
ax.grid()
ax.scatter(date_format, data[variable])
ax.set(xlabel="Date", ylabel=variable, title=name)
date_form = DateFormatter("%d-%m")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
fig.savefig(name + '.png')
plt.show()

# A possible methodology for correcting this systematic bias consists in the 
# calculation of the moving average, which is normally used to analyze time-series 
# by calculating averages of different subsets of the complete dataset

rolling_average_days = 7
data['new_positives_moving'] = data['new_positives'].rolling(window=rolling_average_days).mean()
variable = 'new_positives_moving'
name = "New positive changes"
fig, ax = plt.subplots(figsize=(12, 5))
ax.grid()
ax.scatter(date_format,data[variable])
ax.set(xlabel="Date",ylabel=variable,title=name)
date_form = DateFormatter("%d-%m")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(mdates.DayLocator(interval = 3))
fig.savefig(name + '.png')
plt.show()


data['serious_deaths'] = data['diff_deceased'] + data['diff_swabs']
# prepare the lists for the model
X = date_format
y = data['serious_deaths'].tolist()[1:]
# date format is not suitable for modeling, let's transform the date into incrementals number starting from April 1st
starting_date = 37  # April 1st is the 37th day of the series
day_numbers = []
for i in range(1, len(X)):
    day_numbers.append([i])
X = day_numbers
# # let's train our model only with data after the peak
X = X[starting_date:]
y = y[starting_date:]
# Instantiate Linear Regression
linear_regr = linear_model.LinearRegression()
# Train the model using the training sets
linear_regr.fit(X, y)
print ("Linear Regression Model Score: %s" % (linear_regr.score(X, y)))
