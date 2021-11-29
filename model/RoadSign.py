class RoadSign:
    "Class that models Road Signs"
    def __init__(self,type):
        "Builder of RoadSign class. Parameters: type (type of road sign)."
        self.type=type

    def addPrediction(self,prediction):
        "Method that adds a prediction attribute to a RoadSign object. It is supposed to be executed after a prediction"
        self.prediction=prediction
