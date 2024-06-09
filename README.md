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
1. python_projekt_raport.pdf - project report
2. model.py - file for create, compile, fit and save our machine learning model
3. main.py - file for running chatbot
4. saved_data - folder with files, that contains model, words and classes files
5. dataset - folder with our dataset
6. services - folder with services files
   addiction_service.py - service for any addiction useful code
   json_service.py - service for work with json files, such as reading or writing
   pickle_service.py - services for work with pickle framework that can save or load different files
   ml_model_service.py - service for ML model. Here we are creating, compilint, teaching and saving our AI model
7. variables.py - file with variables, that can be changed during program compilation
8. constants.py - file with constants including filepaths and extensions. Data, that could no be changed

## Tasks

> [!NOTE]
> Here you can find tasks list

- [x] [000] Create tasks list file
- [x] [001] Write in README commit rules
- [x] [002] Write in README branch rules
- [x] [002a] Add in README: Installation, project information, technologies, ...
- [x] [003] Add dataset, add dependencies for frameworks, addarchitecture folders and files
- [x] [004] Implement function to read json dataset with given dataset name
- [x] [005] Add logic with to divide dataset text into words, classes and documents
- [x] [006] Write logic for saving words and classes into binary files in folder ‘saved_data’ 
- [x] [007] Make binary code from input dataset data
- [x] [008] Write code for creating instance (model) with Sequential and configure it
- [x] [009] Compile and save ML Model. Add print in the end of the code to show the end of the 
compiling
- [ ] [010] Extend dataset
- [x] [011] Load saved intents, words, classes and ML Model
- [x] [012] Write function to clean up sentences and function for checking, if word is present in input and return array with '0' and '1'
- [x] [013] Write predict function
- [x] [014] Write function for getting response
- [x] [015] Write function to make infinite chatting
- [x] [016] Add logic to task [015] that can interrupt program in 'bye', 'goodbye' etc. cases

> [!TIP]
> If you need to add, edit or remove task, here are the examples

**case 0**: you need to mark task as finished
**solution**: please, add 'x' into [ ]: 
- [ ] not finished task
- [x] completed task

**case 1**: you need to add task in 006 place
**solution**: please, write [006a] code for it

**case 2**: you need to change task
**solution**: strikethrough previous task and write new with the same code:
- ~~[006] Add logic with to divide dataset text into words, classes and documents~~
- [006] Make refactoring

**case 3**: you need to remove task
**solution**: strikethrough task:
- ~~[006] Add logic with to divide dataset text into words, classes and documents~~
> [!CAUTION]
> ALL CHANGES WITH THIS FILE YOU CAN MAKE ONLY FROM MH-000-Tasks-file BRANCH

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
