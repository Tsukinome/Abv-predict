# BeerRecipePredict

* **ABV**: Technically, alcohol by volume is defined as a standard measure of how much alcohol is contained in a given volume 
  of an alcoholic beverage. It is defined as the number of milliliters (mL) of pure ethanol present in 100 mL of solution at 20°C (68°F).
  The higher the ABV, the boozier a beer will be in its aroma and flavor.
  
* **IBU**: IBUs measure the parts per million of isohumulone found in a beer. 
  Isohumulone is the acid found in hops that gives beer its distinct bitterness. 
  Though the IBU scale can be used as a general guideline for taste, with lower 
  IBUs corresponding to less bitterness and vice versa, 
  it's important to note that malt and other flavors can mask the taste of bitterness in beer.
  
* **SRM:** While not quite as recognizable and widespread as alcohol by volume and international bittering units,
  SRM or Standard Reference Method is about as close as the beer world comes to a unified way of gauging color.
  
* **OG:** Though a wee bit more granular than, say, the easily understood numbers of ABV, IBU and SRM, 
  original gravity is defined as the relative density of the wort – the liquid that will ferment and become beer. 
  That density revolves mostly around the quantity of fermentable sugars in the wort, which are fermented by the yeast 
  and become alcohol. In terms of usefulness, OG is regarded as a guide to the alcoholic strength of the finished beer, 
  but in a more brewer-friendly term.
  
* **FG:** If the fermentation is finished, the specific gravity is called the final gravity (abbreviated FG). 
  For example, for a typical strength beer, OG could be 1.050 and FG could be 1.010.

**Table of content:**
* [Introduction](#introduction)
* [Modeling](#modeling)  
* [Technologies Used](#technologies)
* [License](#license)

### Introduction

The India Pale Ale (IPA) is a beer style of incredible popularity. Beer brewers have scrambled 
in recent years to produce new variations of the style and fill shelves with IPAs. 
As such, the purist definition of IPA as a slightly hoppier pale ale has been considerably stretched.

### Modeling 

The model and its accompanying methods were created and trained using Jupyter Notebook in the Model directory.

### Usage

```/predict``` - Send a POST request to get the model prediction in JSON format.
```/inferences``` - Send a GET request to get the last 10 model inferences in JSON format.

```
import json
import requests

data = json.dumps(
{
    "inputs": [
        {
            "OG":1.055, 
            "FG":1.013,
            "SMR": "19.44",
            "IBU": "4.83",
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
