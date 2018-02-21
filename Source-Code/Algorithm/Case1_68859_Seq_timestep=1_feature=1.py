# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# LSTM for Predicting GPS data
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

'''
Sequential data case
'''

# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset
dataframe = read_csv('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\OUT_RAW_CASE1.csv',engine='python', skipfooter=0)
dataset = dataframe.values
dataset = dataset.astype('float32')

print(dataset.shape)
print(dataset[0:1])
print('OK1')

train_size = int(len(dataset) * 0.80)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

print(train.shape)
print(train[0:2,1])
print('OK2')

look_back = 1 #~~ tương đương LOOK_BACK trong code JAVA ~ CASE này không được thay đổi số này

trainX = train[:,0]
trainY = train[:,1]
testX = test[:,0]
testY = test[:,1]

#print(trainX.shape)

#print(testY)

# reshape input to be [samples, time steps, features] = (trainX.shape[0], 1, 1); còn trainX sẽ là kết quả sau khi reshape
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, 1))
testX = numpy.reshape(testX, (testX.shape[0], 1, 1))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(3, input_shape=(1, look_back))) # input with (1,1) neurons and 1st hidden layer with 13 neurons
model.add(Dense(8)) # 2nd hidden layer with 8 neurons
model.add(Dense(8))
model.add(Dense(1)) # Output with 1 neurons
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=5, batch_size=1, verbose=2)
# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

trainY = numpy.reshape(trainY, (1,trainPredict.shape[0]))

trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
trainScoreMAPE = numpy.mean(numpy.abs((trainY[0] - trainPredict[:,0]) / trainY[0])) * 100
print('Train Score: %.2f RMSE' % (trainScore))
print('Train Score: %.2f percent MAPE' % (trainScoreMAPE))

testY = numpy.reshape(testY, (1,testPredict.shape[0]))

testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
testScoreMAPE = numpy.mean(numpy.abs((testY[0] - testPredict[:,0]) / testY[0])) * 100

print('Test Score: %.2f RMSE' % (testScore))
print('Test Score: %.2f percent MAPE' % (testScoreMAPE))
print(testY.shape)
print(testPredict.shape)

'''
indexval = 0
for i in range(len(testY[0,:])):     
    print(testY[0,indexval])
    indexval += 1
print("-----------")
'''
'''
indexval = 0
for i in range(len(testPredict)):     
    print(testPredict[indexval,0])
    indexval += 1
'''
