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

'''
Sequential data case
'''
look_back = 1 #~ tương đương LOOK_BACK trong code JAVA
# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset
dataframe = read_csv('E:\PhD-Research\Data_Experiment\Non_Cutting_Data\OUT_RAW_CASE2.csv',engine='python', skipfooter=0)
dataset = dataframe.values
dataset = dataset.astype('float32')

print("Shape:")
print(dataset.shape)
print("row: ")
print(dataset[0:1])

train_size = int(len(dataset) * 0.80)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

trainX = train[:,:look_back]
trainY = train[:,look_back]
testX = test[:,:look_back]
testY = test[:,look_back]

# reshape input to be [samples, time steps, features] = (trainX.shape[0], 1, 1); còn trainX sẽ là kết quả sau khi reshape
#trainX = numpy.reshape(trainX, (trainX.shape[0], 1, look_back))
#testX = numpy.reshape(testX, (testX.shape[0], 1, look_back))
trainX = numpy.reshape(trainX, (trainX.shape[0], look_back,1))
testX = numpy.reshape(testX, (testX.shape[0], look_back,1))

# create and fit the LSTM network
model = Sequential()
#model.add(LSTM(3, input_shape=(1, look_back))) # input with look_back neurons and 1st hidden layer with 9 neurons
model.add(LSTM(2, input_shape=(look_back,1)))
#model.add(Dense(2))
#model.add(Dense(10)) #
#model.add(Dense(10)) #
#model.add(Dense(10)) # add hidden layer
model.add(Dense(1)) # output
model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(trainX, trainY, epochs=5, batch_size=8, verbose=2)
# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

trainY = numpy.reshape(trainY, (1,trainPredict.shape[0]))

trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
#trainScoreMAPE = numpy.mean(numpy.abs((trainY[0] - trainPredict[:,0]) / trainY[0])) * 100
#print('Train Score: %.2f percent MAPE' % (trainScoreMAPE))

filterThresh = 10000 #Threshold for delta
speedThresh = 2 #Speed threshold for speed
count_index = 2; #  file raw has header and begin from 1 (not 0)
print("===========TRAINING VALIDATION================")   

size_train = trainY[0].shape[0]
print("Size_train: " + str(size_train))
sum_train = 0
count_train = 0;
count_train_speed = 0;
for itrain in range(0,size_train):
    atrain = trainY[0,itrain]
    ftrain = trainPredict[itrain,0]    
    delta = numpy.abs((atrain - ftrain)/atrain)
    
    if(atrain*65 < speedThresh):
        count_train_speed = count_train_speed + 1
        print('INDEX has speed < '+ str(speedThresh) +': ' + str(count_index))
    
    if(delta <= filterThresh):
        sum_train = sum_train + delta
    
    if delta > filterThresh:
        count_train = count_train + 1
        size_train = size_train - 1
        print(str(atrain * 65) + "-->" + str(ftrain * 65))
        print("delta =" + str(delta))
        
    count_index = count_index + 1

print("===========TRAINING RESULT================")   

print('Train Score: %.2f RMSE' % (trainScore))
print("Number >= "+ str(filterThresh)+": " + str(count_train))
print("Size_test: " + str(size_train))
print("Number of speed < 2: " + str(count_train_speed))
mape_train = sum_train / size_train
print("MAPE:")
print(mape_train)

print("===========TESTING VALIDATION================")   
'#############################################################'
testY = numpy.reshape(testY, (1,testPredict.shape[0]))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
size_test = testY[0].shape[0]
print("Size_test: " + str(size_test))
sum_test = 0
count_test = 0;
count_test_speed = 0;
for itest in range(0,size_test):
    atest = testY[0,itest]
    ftest = testPredict[itest,0]    
    delta = numpy.abs((atest - ftest)/atest)
    
    if(atest*65 < speedThresh):
        count_test_speed = count_test_speed + 1
        print('INDEX has speed < '+ str(speedThresh) +': ' + str(count_index))
    
    if(delta <= filterThresh):
        sum_test = sum_test + delta
    
    if delta > filterThresh:
        count_test = count_test + 1
        size_test = size_test - 1
        print(str(atest * 65) + "-->" + str(ftest * 65))
        print("delta =" + str(delta))
    
    count_index = count_index + 1

print("===========TEST RESULT================")   

print('Test Score: %.2f RMSE' % (testScore))
print("Number >= " + str(filterThresh)+": " + str(count_test))
print("Size_test: " + str(size_test))
print("Number of speed < 2: " + str(count_test_speed))
mape_test = sum_test / size_test
print("MAPE:")
print(mape_test)
print("===========END ALL VALIDATION ON TRAIN & TEST================")   

''' In ra kết quả '''



fileActual = open("E:\PhD-Research\Data_Experiment\Non_Cutting_Data\Actual.csv","w") 
filePredict = open("E:\PhD-Research\Data_Experiment\Non_Cutting_Data\RESULT_CASE2.csv","w") 
 
indexval = 0
for i in range(len(testY[0,:])):     
    #print(testY[0,indexval])
    fileActual.write(str(testY[0,indexval] * 65.0)) 
    fileActual.write("\n")
    indexval += 1
print("-----------")

indexval = 0
for i in range(len(testPredict)):     
    #print(testPredict[indexval,0])
    filePredict.write(str(testPredict[indexval,0]*65.0))
    filePredict.write("\n")
    indexval += 1
    
fileActual.close() 
filePredict.close() 

#summary model
model.summary()

#summary model LSTM
#plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

# list all data in history
#print(history.history.keys())
# summarize history for accuracy
#plt.plot(history.history['acc'])
#plt.plot(history.history['val_acc'])
#plt.title('model accuracy')
#plt.ylabel('accuracy')
#plt.xlabel('epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
#plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()