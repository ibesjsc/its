# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:52:32 2018

@author: Luzec
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

######################################## TESTING #############################
# LOAD MODEL FOR TESTING
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

look_back = 1 #~ tương đương LOOK_BACK trong code JAVA

#Read file data from directory
test_list_file_path = os.listdir('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\TestingData')
test_file = open("resultTesting.csv","w") 
test_file.write("fileName,RMSE,MAPE\n") 

for test_file_path in test_list_file_path:
    # load the dataset
    dataframe = read_csv('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\TestingData\\'+test_file_path,engine='python', skipfooter=0)
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
    
    trainX = train[:,:look_back]
    trainY = train[:,look_back]
    
    trainX = numpy.reshape(trainX, (trainX.shape[0], look_back,1))  
    
    # make predictions
    trainPredict = loaded_model.predict(trainX)
    
    trainY = numpy.reshape(trainY, (1,trainPredict.shape[0]))   
    
    print('File: ' + test_file_path)
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    trainScoreMAPE = numpy.mean(numpy.abs((trainY[0] - trainPredict[:,0]) / trainY[0])) * 100
    print('Train Score: %.2f percent MAPE' % (trainScoreMAPE))

    test_file.write(test_file_path + "," + str(trainScore) +"," + str(trainScoreMAPE)+"\n")

test_file.close()