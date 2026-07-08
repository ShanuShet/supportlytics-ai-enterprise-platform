import joblib

from sklearn.ensemble import RandomForestClassifier


class ModelTrainer:

    def __init__(self):

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

    def train(self, X, y):

        self.model.fit(X, y)

    def save(self, path):

        joblib.dump(self.model, path)