from sklearn.ensemble import RandomForestRegressor


class ResolutionPredictor:

    def __init__(self):

        self.model = RandomForestRegressor(
            random_state=42
        )

    def train(self, X, y):

        self.model.fit(X, y)

    def predict(self, X):

        return self.model.predict(X)