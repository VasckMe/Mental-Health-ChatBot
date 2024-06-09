# required modules 
import pickle

def load(filepath, extension):
    return pickle.load(open(filepath, extension))

def dump(data, filepath, extension):
    pickle.dump(data, open(filepath, extension))