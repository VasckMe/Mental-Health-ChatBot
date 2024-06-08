# required modules 
import json 

def read(filepath):
    intents = json.loads(open(filepath, encoding='utf8').read())
    return intents