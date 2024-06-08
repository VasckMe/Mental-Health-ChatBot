# required modules 
import numpy as np 
import random
import services.addiction_service as addiction_service
from keras.optimizers import SGD 
from keras.layers import Dense, Dropout 
from keras.models import Sequential 
from keras.models import load_model

# optimizer
sgd = SGD(decay = 1e-6, momentum = 0.9, nesterov = True) 

# create ML model instance (object)
def create(data_x, data_y):
    model = Sequential() 
    model.add(Dense(128, input_shape=(len(data_x[0]), ), activation='relu')) 
    model.add(Dropout(0.5)) 
    model.add(Dense(64, activation='relu')) 
    model.add(Dropout(0.5)) 
    model.add(Dense(len(data_y[0]), activation='softmax'))  
    return model