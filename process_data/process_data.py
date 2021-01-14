import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    This function takes the messages_filepath and categories_filepath as arguments,
    loads files, and returns two dataframes
    messages_filepath: The messages filepath (str)
    categories_filepath: The categories filepath (str)
    returns: Two dataframes
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    return messages, categories


def clean_data(df):
    #Assign the dataframes to separate variables
    messages = df[0]
    categories = df[1]

    #Perform cleaning on the categories dataframe
    ids = categories.drop(columns=['categories'])

    #Create a dataframe of the 36 individual category columns
    categories_df = categories
    categories = categories_df['categories'].str.split(pat=";", n=0, expand=True)

    #Merge datasets
    df = ids.merge(categories, left_index=True, right_index=True)
    categories = df

    #Select the first row of the categories dataframe
    row = [i for i in df.iloc[0]]

    #Extract a list of new column names for categories
    category_colnames = [i.replace("-0","").replace("-1","") for i in row[1:]]
    category_colnames.insert(0, 'id')

    #Rename the columns of `categories`
    categories.columns = category_colnames

    for column in categories:
        # set each value to be the last character of the string
        try:
            categories[column] = categories[column].str.split("-").str.get(1)

            # convert column from string to numeric
            categories[column] =  categories[column].astype('int')
        except AttributeError:
            continue

    #Merge messages with the categories
    df = messages.merge(categories, left_on='id', right_on='id')

    #Drop duplicate messages
    df.drop_duplicates(subset=['message'], keep='first', inplace=True)
    return df


def save_data(df, database_filename):
    engine = create_engine('sqlite:///{0}.db'.format(database_filename))
    df.to_sql('{0}'.format(database_filename), engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
