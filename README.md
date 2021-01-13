# Disaster Response Pipeline Project

[![Build Status](https://travis-ci.com/asheone/disaster_response.svg?token=YapLykbwGDS2RPRSsgz8&branch=main)](https://travis-ci.com/asheone/disaster_response)
[![codecov](https://codecov.io/gh/asheone/disaster_response/branch/main/graph/badge.svg?token=2qKmb3B5PA)](https://codecov.io/gh/asheone/disaster_response)</br>

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
