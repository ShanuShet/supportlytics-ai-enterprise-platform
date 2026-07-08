import pandas as pd


class JSONLoader:

    @staticmethod
    def load(file_path: str):

        return pd.read_json(file_path)