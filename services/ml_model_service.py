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

# compile model with parameters
def compile(model):
    model.compile(
        loss='categorical_crossentropy', 
		optimizer=sgd,
        metrics=['accuracy']
        )
        
# predict class in ML model
def predict(model, input_message, classes_list, words_list):
    list = addiction_service.init_binary_list_with_presented_words(input_message, words_list) 
    res = model.predict(np.array([list]))[0] 
    error_threshold = 0.25

    results = [
        [index, error_result] for index, error_result in enumerate(res)  
        if error_result > error_threshold
        ] 

    results.sort(key=lambda x: x[1], reverse=True) 
    return_list = [] 

    for result in results: 
        return_list.append(
            {
                'intent': classes_list[result[0]], 
                'probability': str(result[1])
            }
        ) 
        return return_list

# get model response
def get_response(intents_list, intents_json): 
    tag = intents_list[0]['intent'] 
    list_of_intents = intents_json['intents'] 
    result = "" 
    for intent in list_of_intents: 
        if intent['tag'] == tag: 
            result = random.choice(intent['responses'])   
            break
    return result 

# loading ml model from file
def load(filepath):
    return load_model(filepath)