# required modules 
import numpy as np 
import random
import services.addiction_service as addiction_service
from keras.optimizers import SGD 
from keras.layers import Dense, Dropout 
from keras.models import Sequential 
from keras.models import load_model 