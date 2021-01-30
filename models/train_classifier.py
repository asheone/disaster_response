import sys

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pickle import dump
from datetime import date
import joblib

from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def load_data(database_filepath):
    """
    Returns the X and Y variables
    :param database_filepath: The directory and the filepath (str)
    :return: The X and Y variables dataframes (df)
    """
    engine = create_engine("sqlite:///" + database_filepath)
    df = pd.read_sql_table(
        table_name='DisasterResponse.db',
        con=engine
    )

    X = df['message']
    Y = df.drop(columns=['message', 'original', 'genre']).set_index('id')

    return X, Y


# def tokenize(df, text_column_name):
def normalize(df, text_column_name):
    """
    This function takes the dataframe loaded with the load_data function, and the column name to be normalized.
    :param df: The input dataframe (dataframe)
    :param text_column_name: The list of column names to process (list)
    :return: The normalized dataframe (dataframe)
    """
    for column in text_column_name:
        # Lower the column content
        df[column] = df[column].str.lower()

        # Remove punctuation
        df[column] = df[column].str.replace(r"[^a-zA-Z0-9]", " ")

    return df


def build_model():
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(stop_words='english', max_features=1800)),
                ('tfidf', TfidfTransformer())
            ])),
        ])),

        ('clf', MultiOutputClassifier(RandomForestClassifier(n_estimators=50,
                                                             class_weight='balanced_subsample',
                                                             warm_start=False)))
    ])

    return pipeline


def evaluate_model(model, X_test, Y_test):
    """
    Returns the models evaluation metrics including the accuracy, F1 score etc
    :param model: The model, output from the build_model() function
    :param X_test: The test dataframe input for results evaluation
    :param Y_test: The test dataframe response for results evaluation
    :return: Prints out the evaluation metrics
    """
    y_pred = model.predict(X_test)
    label_accuracy = np.mean(y_pred == Y_test)
    print("Labels accuracy:\n", label_accuracy)
    print("Mean labels accuracy:", np.mean(label_accuracy))


def save_model(model, model_filepath):
    """
    Saves and returns the pkl model file for further distribution
    :param model: The model, output from the build_model() function
    :param model_filepath: The model output filepath (str)
    :return: The The model saved in the .pkl format
    """
    filename = '{0}_{1}.pkl'.format(model_filepath, date.today())
    return joblib.dump(model, open(filename, 'wb'), compress=3)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X[0:15000], Y[0:15000], test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '
              'as the first argument and the filepath of the pickle file to '
              'save the model to as the second argument. \n\nExample: python '
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
