import numpy as np
import json
import pickle
import pandas as pd
from decouple import config

APP_MODEL_PATH_REG = config("APP_MODEL_PATH_REG")
APP_MODEL_PATH_SCALE = config("APP_MODEL_PATH_SCALE")
APP_MODEL_PATH_ENCODE = config("APP_MODEL_PATH_ENCODE")

regressor = pickle.load(open(APP_MODEL_PATH_REG, "rb"))
scaler = pickle.load(open(APP_MODEL_PATH_SCALE, "rb"))
encoder = pickle.load(open(APP_MODEL_PATH_ENCODE, "rb"))

def transform_data(df: pd.DataFrame) -> np.array:
    """This method prepares dataframe by encoding categorical features
    and scaling numeric features, then returns prepared data for predictions
    :param df: pandas Dataframe with feature columns
    :return: numpy array with processed features data
    """
    categorical_encoded_data = encoder.transform(
        df["type"].values
    ).toarray()
    scaled_numerical_data = scaler.transform(
        df.drop("type", axis=1)
    )
    processed_data = np.concatenate(
        (categorical_encoded_data, scaled_numerical_data), axis=1
    )
    return processed_data

def process_input(request_data: str) -> np.array:
    """Loads a post request body as json, converts it to
    features dataframe calls a method that process it and returns
    the result.
    :param request_data: json structured request body
    :return: processed numpy array
    """
    list_of_dicts = json.loads(request_data)["inputs"]
    features = pd.DataFrame(list_of_dicts)
    processed_data = transform_data(features)
    return processed_data

def predict(input_params) -> np.array:
    """Load model and make a predictions and return
    a numpy array of them.
    :return: predictions numpy array
    """
    predictions = regressor.predict(input_params)
    predictions = np.maximum(5, predictions)
    return predictions