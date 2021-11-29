
from flask import request
#### render_template, redirect, url_for,abort

from model.RoadSign import RoadSign
from model.PredictionModelObject import PredictionModelObject

def test():
    "Controller of testing purposes"
    return "MVC en Flask exitoso"

def predict():
    image = request.files['image']
    prediction = PredictionModelObject.single_predict(image)
    roadSign = RoadSign(request.files['type'])
    roadSign.addPrediction(prediction['category'])
    return roadSign