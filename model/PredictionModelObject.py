from fastai.basic_train import load_learner
from fastai.vision import open_image

class PredictionModelObject:
        model="model_roadsign.pkl"
        learner = load_learner(path='./prediction_model', file=model)
        classes = learner.data.classes


        def single_predict(self,img_file):
            'function to take image and return prediction'
            prediction = self.learner.predict(open_image(img_file))
            probs_list = prediction[2].numpy()
            return {
                'category': self.classes[prediction[1].item()],
                'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(self.classes)}
            }