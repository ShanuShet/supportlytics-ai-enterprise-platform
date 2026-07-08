from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


class ModelEvaluator:

    @staticmethod
    def evaluate(model, X_test, y_test):

        predictions = model.predict(X_test)

        return {

            "accuracy": accuracy_score(
                y_test,
                predictions
            ),

            "report": classification_report(
                y_test,
                predictions,
                output_dict=True
            )

        }