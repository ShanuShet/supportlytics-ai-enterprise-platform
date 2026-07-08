import pandas as pd


class DataPreprocessor:

    @staticmethod
    def preprocess(df: pd.DataFrame):

        df = df.copy()

        df = df.fillna("Unknown")

        df.columns = [

            column.strip().lower().replace(" ", "_")

            for column in df.columns

        ]

        return df