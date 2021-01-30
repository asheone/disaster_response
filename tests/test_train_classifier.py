import os
import os.path
from models.train_classifier import load_data, build_model, main
from sklearn.pipeline import Pipeline

directory = os.path.abspath(os.getcwd()).replace("/tests", "") + ""
db_name = "DisasterResponse"
table_name = ""


def test_if_the_file_exist():
    filename = [db_name]
    for file in filename:
        if os.path.isfile(file):
            print("File {0} Exists!!".format(file))
        else:
            print("File {0} does not exist!!".format(file))


def test_load_data_is_returning_one_entity():
    assert len(load_data("{0}/{1}".format(directory, db_name))) != 0


def test_load_data_is_dataframe():
    assert isinstance(load_data("{0}/{1}".format(directory, db_name)),
                      tuple), "The messages file doesn't return a dataframe"


def test_build_model_returns_pipeline():
    assert isinstance(build_model(), Pipeline)


def test_build_model_is_not_empty():
    assert build_model() != 0


def test_main_is_dataframe():
    assert main() != 0
