import re
import sys
from datetime import date
from functools import partial

import joblib
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sqlalchemy import create_engine

nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])


def load_data(database_filepath):
    """
    Returns the X and Y variables
    :param database_filepath: The directory and the filepath (str)
    :return: The X and Y variables dataframes (df)
    """
    engine = create_engine("sqlite:///" + database_filepath)
    df = pd.read_sql_table(
        table_name='DisasterResponse',
        con=engine
    )

    X = df['message']
    Y = df.drop(columns=['message', 'original', 'genre']).set_index('id')

    return X, Y


def tokenize(text):
    """
    This function takes the dataframe loaded with the load_data function, and the column name to be normalized.
    :param text: The input text from the dataframe (dataframe)
    :return: The normalized dataframe (dataframe)
    """
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip().replace(r"[^a-zA-Z0-9]", " ")
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect',
                 CountVectorizer(tokenizer=partial(tokenize), stop_words='english', max_features=1800)),
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
    print(classification_report(Y_test, y_pred, digits=3, target_names=Y_test.columns))


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
