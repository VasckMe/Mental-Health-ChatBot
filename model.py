# required modules 
import random 
import numpy as np 
import constants 
import variables
import services.json_service as json_service
import services.addiction_service as addiction_service
import services.pickle_service as pickle_service
import services.ml_model_service as model_service
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer() 

# [004] Implement function to read json dataset with given dataset name
intents = json_service.read(constants.dataset_filepath)

# [005] Add logic with to divide dataset text into words, classes and documents

addiction_service.fillListsWithData(intents)
  
# store root words or lemma + sort
variables.words = [
    lemmatizer.lemmatize(variables.word) 
    for variables.word in variables.words if variables.word not in variables.ignore_letters
    ] 
variables.words = sorted(set(variables.words)) 

# [006] Write logic for saving words and classes into binary files in folder ‘saved_data’ 

pickle_service.dump(variables.words, constants.words_filepath, constants.extension_to_write_data_files)
pickle_service.dump(variables.classes, constants.classes_filepath, constants.extension_to_write_data_files)
# [007] Make binary code from input dataset data
addiction_service.convert_into_binary(variables.documents)
  
# split the data 
train_x = list(variables.training[:, 0]) 
train_y = list(variables.training[:, 1]) 

# [008] Write code for creating instance (model) with Sequential and configure it

model = model_service.create(train_x, train_y)

# [009] Compile and save ML Model. Add print in the end of the code to show the end of the 
model_service.compile(model)
fit_model = model_service.fit(model, train_x, train_y)
model_service.save(model, fit_model, constants.model_filepath)
print ("model gotów do użycia")
# compiling
