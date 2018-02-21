# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# LSTM for Predicting GPS data
import numpy
#import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
#from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt
import os
from keras.models import model_from_json

#Read file data from directory
list_file_path = os.listdir('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\TrainingData')

look_back = 1 #~ tương đương LOOK_BACK trong code JAVA
# fix random seed for reproducibility
numpy.random.seed(7)

batch_size=1  

# create and fit the LSTM network
model = Sequential()
#model.add(LSTM(3, input_shape=(1, look_back))) # input with look_back neurons and 1st hidden layer with 9 neurons
model.add(LSTM(2, input_shape=(look_back, 1)))
#model.add(Dense(2))
#model.add(Dense(10)) #
#model.add(Dense(10)) #
#model.add(Dense(10)) # add hidden layer
model.add(Dense(1)) # output
model.compile(loss='mean_squared_error', optimizer='adam')

file = open("resultTraining.csv","w") 
file.write("fileName,RMSE,MAPE\n") 

for file_path in list_file_path:
    # load the dataset
    dataframe = read_csv('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\TrainingData\\'+file_path,engine='python', skipfooter=0)
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    
    print("Shape:")
    print(dataset.shape)
    print("row: ")
    print(dataset[0:1])
    
    train_size = int(len(dataset) * 1.0)
    train = dataset[0:train_size,:]
    trainX = train[:,:look_back]
    trainY = train[:,look_back]
    
    trainX = train[:,:look_back] # Training data
    trainY = train[:,look_back] # Actual result
    
    trainX = numpy.reshape(trainX, (trainX.shape[0], look_back,1))  
    
    history = model.fit(trainX, trainY, epochs=100, batch_size=batch_size, verbose=2)
        
    # make predictions
    trainPredict = model.predict(trainX)
    
    trainY = numpy.reshape(trainY, (1,trainPredict.shape[0]))   
    
    print('File: ' + file_path)
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    trainScoreMAPE = numpy.mean(numpy.abs((trainY[0] - trainPredict[:,0]) / trainY[0])) * 100
    print('Train Score: %.2f percent MAPE' % (trainScoreMAPE))

    file.write(file_path + "," + str(trainScore) +"," + str(trainScoreMAPE)+"\n") 

file.close()

# SAVE Model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

