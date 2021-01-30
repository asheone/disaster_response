import pandas as pd
import os
import os.path
from process_data.process_data import load_data, clean_data, save_data, main

directory = os.path.abspath(os.getcwd()) + "/process_data/"


def test_if_the_file_exist():
    filename = ["disaster_messages.csv", "disaster_categories.csv"]
    for file in filename:
        if os.path.isfile(file):
            print("File {0} Exists!!".format(file))
        else:
            print("File {0} does not exists!!".format(file))


def test_load_data_is_returning_two_entities():
    assert len(
        load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))) == 2


def test_load_data_is_dataframe():
    assert isinstance(
        load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))[0],
        pd.DataFrame), "The messages file doesn't return a dataframe"
    assert isinstance(
        load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))[1],
        pd.DataFrame), "The categories file doesn't return a dataframe"


def test_clean_data_is_dataframe():
    assert isinstance(clean_data(
        load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))),
                      pd.DataFrame), "The function doesn't return a dataframe"


def test_clean_data_is_not_empty_dataframe():
    assert not clean_data(load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(
        directory))).empty, "The function returns empty dataframe"


def test_save_data():
    try:
        assert isinstance(save_data(
            clean_data(
                load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))),
            "DisasterResponse"),
            pd.DataFrame), "The function doesn't return a dataframe"
    except ValueError:
        pass


def test_main_is_printing_results():
    assert main()!=0