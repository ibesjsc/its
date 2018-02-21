# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 23:45:16 2018

@author: Luzec
"""

from pandas import read_csv
import numpy
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error


series = read_csv('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\\TestARIMA.csv', header=0, squeeze=True)
X = series.values
X = X.astype('float32')
print(series.head())
series.plot()
pyplot.show()


size = int(len(X) * 0.80)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

count  = 0

for t in range(len(test)):
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)    
    delta = numpy.abs((obs - yhat) / obs)
    if(delta > 1) :
        print('predicted=%f, expected=%f' % (yhat, obs))
        count = count + 1
       

print(count)

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

trainScoreMAPE = numpy.mean(numpy.abs((test - predictions) /test)) * 100
print('Train Score: %.2f percent MAPE' % (trainScoreMAPE))
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()