import numpy as np
import json
import pickle
import pandas as pd
from decouple import config

APP_MODEL_PATH_SCALE = config("APP_MODEL_PATH_SCALE")
scaler = pickle.load(open(APP_MODEL_PATH_SCALE, "rb"))

def process_input(request_data: str) -> np.array:
    """Loads a post request body as json, converts it to
    features dataframe calls a method that process it and returns
    the result.
    :param request_data: json structured request body
    :return: processed numpy array
    """
    list_of_dicts = json.loads(request_data)["inputs"]
    features = pd.DataFrame(list_of_dicts)
    processed_data = scaler.transform(features)
    return processed_data