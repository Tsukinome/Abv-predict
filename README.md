# Beer ABV Predict

This is the second part of capstone project in Turing College.
Model was trained on https://www.brewersfriend.com/ parameters: 
IBU, SRM, OG, FG, beer type and can predict ABV of a beer.

**Table of content:**
* [Introduction](#introduction)
* [Modeling](#modeling)  
* [Technologies Used](#technologies)
* [License](#license)

### Introduction

Beer brewers have scrambled  in recent years to produce new variations of the beer styles. 
As such, the purest definition of beer styles has been considerably stretched. When brewing your own beer
there is no telling exactly what ABV will be present. Predicting ABV of yet to be beer can be 
useful when producing in big quantities.

### Modeling 

The model and its accompanying methods were created and trained using Jupyter Notebook in the Models directory.

### Usage

```/predict``` - Send a POST request to get the model prediction in JSON format.
```/last_requests``` - Route to return most recent requests and responses in 
JSON format. Returns 10 as default but can be any number if specified.

You can send the requests using a tool like 
Postman or you can do it with programming language. Here is a Python example:
```
import json
import requests

data = json.dumps(
{
    "inputs": [
        {
            "OG": 1.055, 
            "FG": 1.013,
            "SMR": 19.44,
            "IBU": 4.83,
            "type": "Cream ale"
        }
    ]
})

resp = requests.post('https://beer-predict.herokuapp.com/predict', data=data)
print(resp.text)

```

### Technologies
For the used packages and technologies view the [requirements.txt](requirements.txt) file.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
