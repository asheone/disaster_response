# Disaster Response Pipeline Project

[![Build Status](https://travis-ci.com/asheone/disaster_response.svg?token=YapLykbwGDS2RPRSsgz8&branch=main)](https://travis-ci.com/asheone/disaster_response)
[![codecov](https://codecov.io/gh/asheone/disaster_response/branch/main/graph/badge.svg?token=2qKmb3B5PA)](https://codecov.io/gh/asheone/disaster_response)</br>

<b>TODO: </br>
1. DONE Add ###Brief project description
2. DONE Add the docstrings to the functions
3. Add the normalize, lemmatize, and tokenize into the train_claasifier.py file
4. Explain in the description that GridSearch was used for finding the best model, but then only the best model is used in the resulting model.
5. Output the f1 score, precision and recall for each category
6. Include at least two visualizations using data from the SQLite database in the main page

### Project description </b></br>
This project is a submission for the Udacity Data Science course.
The main gola was to prepare the input messages and categoris files, perform the cleaning, find and build the best performing model, and output the results using  Flask. The main output is the website with the model implemented under the hood, which is classifing the message into one or more out of 26 disaster categories.

### <b> Instructions: </b></br>
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database, run this line in the `process_data` folder: </br>
        `python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves run this line in the `models` folder: </br>
        `python train_classifier.py ../process_data/DisasterResponse.db ../classifier`
    - To run the tests, run this line in the main folder: </br>
        `pytest`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
