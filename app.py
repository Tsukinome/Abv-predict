from flask import Flask, request
import json
from Src.process import process_input
from Heroku.database import Database
from decouple import config
import pickle

database = Database()
APP_MODEL_PATH_REG = config("APP_MODEL_PATH_REG")
regressor = pickle.load(open(APP_MODEL_PATH_REG, "rb"))

app = Flask(__name__)

@app.route("/")
def index() -> str:
    """
    Creates a route to return the note that connection is established.
    :return: connection status
    """
    try:
        return "Connection established"
    except:
        return "There was a problem loading the app"


@app.route("/predict", methods=["POST"])
def predict() -> str:
    """
    Creates a route to return the prediction given the user inputs.
    :return: list of predictions of the ABV
    """
    user_input = request.data

    try:
        input_params = process_input(user_input)
        predictions = regressor.predict(input_params)
        output = json.dumps({"Predicted ABV": predictions.tolist()})

    except Exception as e:
        output = json.dumps({"Error": f"Prediction failed: {e}"})
        return output, 200

    finally:
        database.create_record(user_input.decode(), output)


@app.route("/last_requests", methods=["GET"], defaults={"records": 10})
def last_requests(records: int) -> list:
    """
    Creates route to return a specified number of last requests made using the API. Returns 10 requests by default.
    :param records: the number of last requests to be returned (int)
    :return: the number of last requests made using the API
    """

    retrieved_requests = database.get_recent_records(records)

    return json.dumps({"last_requests": retrieved_requests}), 200


if __name__ == "__main__":
    app.run()