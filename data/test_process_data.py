import pandas as pd
from process_data import load_data, clean_data, save_data


def test_load_data_is_returning_two_entities():
    assert len(load_data('/data/disaster_messages.csv', 'categories.csv'))==2


def test_load_data_is_dataframe():
    assert isinstance(load_data('/data/disaster_messages.csv', '/data/disaster_categories.csv')[0], pd.DataFrame), "The messages file doesn't return a dataframe"
    assert isinstance(load_data('/data/disaster_messages.csv', '/data/disaster_categories.csv')[1], pd.DataFrame), "The categories file doesn't return a dataframe"


def test_clean_data_is_dataframe():
    assert isinstance(clean_data(load_data('/data/disaster_messages.csv', '/data/disaster_categories.csv')), pd.DataFrame), "The function doesn't return a dataframe"

def test_clean_data_is_not_empty_dataframe():
    assert not clean_data(load_data('/data/disaster_messages.csv', '/data/disaster_categories.csv')).empty, "The function returns empty dataframe"
