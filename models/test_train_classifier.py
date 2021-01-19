import pandas as pd
import os
import os.path
# from process_data.process_data import load_data, clean_data, save_data
from models.train_classifier import load_data, normalize

directory = os.path.abspath(os.getcwd()).replace("/models","")  + "/process_data"
db_name = "DisasterResponse.db"


def test_if_the_file_exsist():

    filename = [db_name]
    for file in filename:
        if(os.path.isfile(file)):
          print("File {0} Exists!!".format(file))
        else:
          print("File {0} does not exists!!".format(file))


def test_load_data_is_returning_one_entity():
    assert len(load_data("{0}/{1}".format(directory, db_name)))!=0


def test_load_data_is_dataframe():
    assert isinstance(load_data("{0}/{1}".format(directory, db_name)), pd.DataFrame), "The messages file doesn't return a dataframe"


def test_normalize_is_dataframe():
    assert isinstance(normalize(load_data("{0}/{1}".format(directory, db_name)), ["message"]), pd.DataFrame), "The function doesn't return a dataframe"


# def test_clean_data_is_not_empty_dataframe():
#     assert not clean_data(load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))).empty, "The function returns empty dataframe"
#
#
# def test_save_data():
#     assert isinstance(save_data(
#         clean_data(
#             load_data("{0}/disaster_messages.csv".format(directory), "{0}/disaster_categories.csv".format(directory))), "DisasterResponse"),
#                       pd.DataFrame), "The function doesn't return a dataframe"
