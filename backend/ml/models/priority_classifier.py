from sklearn.ensemble import RandomForestClassifier


class PriorityClassifier:

    def __init__(self):

        self.model = RandomForestClassifier(
            random_state=42
        )

    def train(self, X, y):

        self.model.fit(X, y)

    def predict(self, X):

        return self.model.predict(X)