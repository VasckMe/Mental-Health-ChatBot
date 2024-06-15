# required modules 
import constants
import services.json_service as json_service
import services.pickle_service as pickle_service
import services.ml_model_service as model_service

# load saved intents, words, classes and ML Model
intents = json_service.read(constants.dataset_filepath)
words = pickle_service.load(constants.words_filepath, constants.extension_to_read_data_files)
classes = pickle_service.load(constants.classes_filepath, constants.extension_to_read_data_files)
model = model_service.load(constants.model_filepath)

# infinite chatting
while True:
    userText = input('User: ')
    # predict
    predicted_class = model_service.predict(model, userText, classes, words)
    result = model_service.get_response(predicted_class, intents)

    if predicted_class[0]["intent"] == "goodbye":
        print('Chatbot:', result)
        break

    print('Chatbot:', result)