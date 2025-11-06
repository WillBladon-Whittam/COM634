import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
import warnings
from sklearn.metrics import mean_squared_error
from statsmodels.tools.eval_measures import rmse
from statsmodels.tsa.stattools import adfuller
from numpy import log
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima.arima.utils import ndiffs
import statsmodels.api as sm
import matplotlib.pyplot as plt


warnings.filterwarnings("ignore")


airline = pd.read_csv('AirPassengers.csv',
 index_col ='Month',
 parse_dates = True)

# Show first 10 rows of the data
airline.head(10)

# ETS Decomposition
ets = seasonal_decompose(airline['#Passengers'], model ='multiplicative')
ets.plot()

# Fit auto_arima function to AirPassengers dataset
stepwise_fit = auto_arima(airline['#Passengers'], start_p = 1, start_q = 1,
 max_p = 3, max_q = 3, m = 12,
 start_P = 0, seasonal = True,
 d = None, D = 1, trace = True,
 error_action ='ignore', # we don't want to know if an order does not work
 suppress_warnings = True, # we don't want convergence warnings
 stepwise = True) # set to stepwise

# To print the summary
stepwise_fit.summary()

# Split data into train / test sets
train = airline.iloc[:len(airline)-12]
test = airline.iloc[len(airline)-12:] # set one year(12 months) for testing

# Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) on the training set
model = SARIMAX(train['#Passengers'],
 order = (0, 1, 1),
 seasonal_order =(2, 1, 1, 12))

result = model.fit()
result.summary()

start = len(train)
end = len(train) + len(test) - 1

# Predictions for one-year against the test set
predictions = result.predict(start, end,
 typ = 'levels').rename("Predictions")

# plot predictions and actual values
predictions.plot(legend = True)
test['#Passengers'].plot(legend = True)

# Calculate root mean squared error
print ("rmse = ",rmse(test["#Passengers"], predictions))

# Calculate mean squared error
print ("mse = ", mean_squared_error(test["#Passengers"], predictions))

# Train the model on the full dataset
model = model = SARIMAX(airline['#Passengers'],
 order = (0, 1, 1),
 seasonal_order =(2, 1, 1, 12))
result = model.fit()

# Forecast for the next 3 years
forecast = result.predict(start = len(airline),
 end = (len(airline)-1) + 3 * 12,
 typ = 'levels').rename('Forecast')

# Plot the forecast values
airline['#Passengers'].plot(figsize = (12, 5), legend = True)
forecast.plot(legend = True)

mydata = pd.read_csv('AirPassengers.csv', index_col = 'Month', parse_dates = True)

res = adfuller(mydata['#Passengers'])
print('Augmented Dickey-Fuller Statistic: %f' % res[0])
print('p-value: %f' % res[1]) 

plt.rcParams.update({'figure.figsize' : (9,7), 'figure.dpi' : 120})

# Importing data
df = pd.read_csv('AirPassengers.csv', index_col = 'Month', header = 0, parse_dates = True)

# The Genuine Series
fig, axes = plt.subplots(3, 2, sharex = True)
axes[0, 0].plot(df['#Passengers']); axes[0, 0].set_title('The Genuine Series')
plot_acf(df['#Passengers'], ax = axes[0, 1])

# Order of Differencing: First
axes[1, 0].plot(df['#Passengers'].diff()); axes[1, 0].set_title('Order of Differencing: First')
plot_acf(df['#Passengers'].diff().dropna(), ax = axes[1, 1])

# Order of Differencing: Second
axes[2, 0].plot(df['#Passengers'].diff().diff()); axes[2, 0].set_title('Order of Differencing: Second')
plot_acf(df['#Passengers'].diff().diff().dropna(), ax = axes[2, 1])

X = df['#Passengers']

# Augmented Dickey Fuller Test
adftest = ndiffs(X, test = 'adf')

# KPSS Test
kpsstest = ndiffs(X, test = 'kpss')

# PP Test
pptest = ndiffs(X, test = 'pp')

print("ADF Test =", adftest)
print("KPSS Test =", kpsstest)
print("PP Test =", pptest)

plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex = True)
axes[0].plot(df['#Passengers'].diff()); axes[0].set_title('Order of Differencing: First')
axes[1].set(ylim = (0,5))
plot_pacf(df['#Passengers'].diff().dropna(), ax = axes[1])

plt.rcParams.update({'figure.figsize' : (9,3), 'figure.dpi' : 120})
# Creating ARIMA model
mymodel = sm.tsa.arima.ARIMA(df['#Passengers'], order=(1,1,1))
modelfit = mymodel.fit()

# Plotting Residual Errors
myresiduals = pd.DataFrame(modelfit.resid)
fig, ax = plt.subplots(1,2)
myresiduals.plot(title = "Residuals", ax = ax[0])
myresiduals.plot(kind = 'kde', title = 'Density', ax = ax[1])

plt.show()