# required modules 
import variables
import nltk 
import numpy as np 
import random

def fillListsWithData(data_list):
    for intent in data_list['intents']: 
        for pattern in intent['patterns']: 
            word_list = nltk.word_tokenize(pattern) # separate words in pattern, make list from them
            variables.words.extend(word_list) # add list into words array
            
            # associate patterns with respective tags 
            variables.documents.append(((word_list), intent['tag'])) 
    
            # append the tags to the class list 
            if intent['tag'] not in variables.classes: 
                variables.classes.append(intent['tag']) 

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

# function for lemmatizing words from sentence (looking for root word)
def clean_up_sentences(sentence): 
    lemmatizer = nltk.stem.WordNetLemmatizer() 

    sentence_words = nltk.word_tokenize(sentence) 
    sentence_words = [
        lemmatizer.lemmatize(word)  
        for word in sentence_words
        ] 
    return sentence_words

