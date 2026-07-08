import joblib


class PredictionEngine:

    def __init__(self, model_path):

        self.model = joblib.load(model_path)

    def predict(self, sample):

        return self.model.predict(sample)

    def predict_probability(self, sample):

        return self.model.predict_proba(sample)