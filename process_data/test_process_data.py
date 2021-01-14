import pandas as pd
import os
import os.path
from process_data.process_data import load_data, clean_data, save_data

directory = os.getcwd()

def test_if_the_file_exsist():

    filename = ["disaster_messages.csv", "categories.csv"]
    for file in filename:
        if(os.path.isfile(file)):
          print("File {0} Exists!!".format(file))
        else:
          print("File {0} does not exists!!".format(file))

def test_load_data_is_returning_two_entities():
    assert len(load_data("{0}/disaster_messages.csv".format(directory), "{0}/categories.csv".format(directory)))==2


def test_load_data_is_dataframe():
    assert isinstance(load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))[0], pd.DataFrame), "The messages file doesn't return a dataframe"
    assert isinstance(load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))[1], pd.DataFrame), "The categories file doesn't return a dataframe"


def test_clean_data_is_dataframe():
    assert isinstance(clean_data(load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))), pd.DataFrame), "The function doesn't return a dataframe"

def test_clean_data_is_not_empty_dataframe():
    assert not clean_data(load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))).empty, "The function returns empty dataframe"
