# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 03:11:39 2017

@author: Luzec
"""

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
dataframe = read_csv('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\OUT_RAW_CASE3.csv',engine='python', skipfooter=0)
dataset = dataframe.values
dataset = dataset.astype('float32')

print(dataset.shape)
print(dataset[0:1])
print('OK1')

train_size = int(len(dataset) * 0.80)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

#print(train.shape)
#print(train[0:2,1])
#print('OK2')

k= 2 #frame-Seq
number_time_step = 4 #time_step ~ number of step in past #~ tương đương LOOK_BACK trong code JAVA
look_back = k*number_time_step #number feature

trainX = train[:,:look_back]
trainY = train[:,look_back]
testX = test[:,:look_back]
testY = test[:,look_back]

#print(trainX)
#print(trainY)
print(trainX.shape)

#print(testY)

# reshape input to be [samples, time steps, features] = (trainX.shape[0], 1, 1); còn trainX sẽ là kết quả sau khi reshape
#trainX = numpy.reshape(trainX, (trainX.shape[0], number_time_step, k)) # *chỗ này
#testX = numpy.reshape(testX, (testX.shape[0], number_time_step, k)) # *chỗ này

# create and fit the LSTM network
model = Sequential()
#model.add(LSTM(9, input_shape=(number_time_step, k))) # *chỗ này
model.add(Dense(1, input_dim=look_back, activation='relu'))
model.add(Dense(13, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(trainX, trainY, epochs=50, batch_size=1, verbose=2)
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

''' In ra kết quả '''

filePredict = open("E:\PhD-Research\Data_Experiment\Non_Cutting_Data\RESULT_CASE3.csv","w") 
indexval = 0
for i in range(len(testY[0,:])):     
    #print(testY[0,indexval])
    indexval += 1
print("-----------")


indexval = 0
for i in range(len(testPredict)):     
    #print(testPredict[indexval,0])
    filePredict.write(str(testPredict[indexval,0]*65.0))
    filePredict.write("\n")
    indexval += 1

filePredict.close() 
