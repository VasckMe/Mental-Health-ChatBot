# Mental-Health-ChatBot

This repository contains simple chatbot for mental health chatting.
Chatbot teached by small dataset intents.json and can be used from your IDE and terminal.

![Screen Recording 2024-06-09 at 5 19 50 PM](https://github.com/VasckMe/Mental-Health-ChatBot/assets/110229952/0ca583b7-0e93-4043-a87e-01913a1fefe8)

## Framework requirements
- tensorflow, keras
- numpy, nltk

## Installation

If you don't have python, install it:
Windows: https://www.digitalocean.com/community/tutorials/install-python-windows-10
macOS: https://www.dataquest.io/blog/installing-python-on-mac/

### macOS
1. Clone repository
2. Open repository folder with your terminal
3. Write in terminal:
```
python3 -m venv myenvironment
source myenvironment/bin/activate
```
4. Install all required frameworks:
```
pip3 install tensorflow keras nltk numpy

If you don't have pip3, install it with:

brew install python3
```
5. Run model.py file:
```
python3 model.py
```
6. Run main.py file:
```
python3 model.py
```

### Windows
1. Clone repository
2. Open repository folder with your terminal
3. Install all required frameworks:
```
pip install tensorflow keras nltk numpy
```
4. Run model.py file:
```
python model.py
```
5. Run main.py file:
```
python main.py
```

## Repository descripton

1. model.py - file for create, compile, fit and save our machine learning model
2. main.py - file for running chatbot
3. saved_data - folder with files, that contains model, words and classes files
4. dataset - folder with our dataset
5. services - folder with services files
   addiction_service.py - service for any addiction useful code
   json_service.py - service for work with json files, such as reading or writing
   pickle_service.py - services for work with pickle framework that can save or load different files
   ml_model_service.py - service for ML model. Here we are creating, compilint, teaching and saving our AI model
6. variables.py - file with variables, that can be changed during program compilation
7. constants.py - file with constants including filepaths and extensions. Data, that could no be changed


## Branch ruless
```
1. Don't remove "main" or "develop" branches
2. Branch title must has:
    - code of the project
    - task number
    - task title
3. If you finish task, make Pull Request into develop branch (Optional)
4. If develop has updates, merge it into your branch. Your branch should be up to date with develop!
```
## Commit rules
```
1. Commit title is necessary to fill
2. Commit title must has:
    - code of the project (MH)
    - task number (000 - 999, check in TASKS.md)
    - text with root words about work
3. Commit description is optional. Write description about changes in commit, if you need
```
