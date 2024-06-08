# required modules 
import constants
import services.json_service as json_service
import services.pickle_service as pickle_service
import services.ml_model_service as model_service

# [011] Load saved intents, words, classes and ML Model

intents = json_service.read(constants.dataset_filepath)

# # print(intents)
# import pickle
# words = pickle.load(open("saved_data/words.pkl", "rb"))
# classes = pickle.load(open("saved_data/classes.pkl", "rb"))

# from keras.models import load_model

# model = load_model("saved_data/chatbotmodel.h5")



# [012] Write function to clean up sentences and function for checking, if word is present in input and return array with '0' and '1'

# [015] Write function to make infinite chatting
while True:
    userText = input('User: ')

    # [013] Write predict function

    # [014] Write function for getting response

# [016] Add logic to task [015] that can interrupt program in 'bye', 'goodbye' etc. cases