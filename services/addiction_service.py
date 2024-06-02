# required modules 
import variables
import nltk 
import numpy as np 
import random

def convert_into_binary(documents):
    output_empty = [0]*len(variables.classes) 
    lemmatizer = nltk.stem.WordNetLemmatizer() 

    for document in documents: 
        bag = [] 
        word_patterns = document[0] 
        word_patterns = [lemmatizer.lemmatize( 
            word.lower()) for word in word_patterns] 
        for word in variables.words: 
            bag.append(1) if word in word_patterns else bag.append(0) 
        
        output_row = list(output_empty) 
        output_row[variables.classes.index(document[1])] = 1
        variables.training.append([bag, output_row]) 
    
    random.shuffle(variables.training) 
    variables.training = np.array(variables.training, dtype="object")