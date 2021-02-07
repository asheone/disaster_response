# Disaster Response Pipeline Project

[![Build Status](https://travis-ci.com/asheone/disaster_response.svg?token=YapLykbwGDS2RPRSsgz8&branch=main)](https://travis-ci.com/asheone/disaster_response)
[![codecov](https://codecov.io/gh/asheone/disaster_response/branch/main/graph/badge.svg?token=2qKmb3B5PA)](https://codecov.io/gh/asheone/disaster_response)</br>

<b>TODO: </br>

4. Explain in the description that GridSearch was used for finding the best model, but then only the best model is used in the resulting model.
6. Include at least two visualizations using data from the SQLite database in the main page

### Project description </b></br>
This project is a submission for the Udacity Data Science course.
The main goal was to prepare the input messages and categoris files, perform the cleaning, find and build the best performing model, and output the results using  Flask. The main output is the website with the model implemented under the hood, which is classifing the message into one or more out of 26 disaster categories.

### Catalog structure </b></br>
There are 4 main catalogs in the repository: `app`, `models`, `process_data`, and `tests`.
The `app` folder contains all the files related to setting up the flask app, so the underlying model can be run on the web browser.
The `models` folder contains the `train_classifier.py` file which holds all the steps required for training the classification model.
The `process_data` folder contains all the steps required for the dataframe cleaning and returns merged datasets, ready for classification training.
The `tests` model holds all the unit tests.


### <b> Instructions: </b></br>
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database, run this line in the `disaster_response` folder: </br>
        `python process_data/process_data.py process_data/disaster_messages.csv process_data/disaster_categories.csv ./DisasterResponse`
    - To run ML pipeline that trains classifier and saves run this line in the `models` folder: </br>
        `python train_classifier.py ../DisasterResponse.db ../classifier`
    - To run the tests, run this line in the main folder: </br>
        `pytest`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
