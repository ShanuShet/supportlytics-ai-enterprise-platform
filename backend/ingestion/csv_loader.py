import pandas as pd


class CSVLoader:

    @staticmethod
    def load(file_path: str):

        return pd.read_csv(file_path)