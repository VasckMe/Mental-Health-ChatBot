# required modules 
import constants
import services.json_service as json_service
import services.pickle_service as pickle_service
import services.ml_model_service as model_service

# [011] Load saved intents, words, classes and ML Model

intents = json_service.read(constants.dataset_filepath)
words = pickle_service.load(constants.words_filepath, constants.extension_to_read_data_files)
classes = pickle_service.load(constants.classes_filepath, constants.extension_to_read_data_files)
model = model_service.load(constants.model_filepath)

# [015] Write function to make infinite chatting
while True:
    userText = input('User: ')
    # [012] Write function to clean up sentences and function for checking, if word is present in input and return array with '0' and '1'
    # [013] Write predict function
    # [014] Write function for getting response
    predicted_class = model_service.predict(model, userText, classes, words)
    result = model_service.get_response(predicted_class, intents)
    print('Chatbot:', result)

# [016] Add logic to task [015] that can interrupt program in 'bye', 'goodbye' etc. cases