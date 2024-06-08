# required modules 
import pickle

def load(filepath, extension):
    return pickle.load(open(filepath, extension))
