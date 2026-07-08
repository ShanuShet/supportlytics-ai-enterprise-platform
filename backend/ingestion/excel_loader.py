import pandas as pd


class ExcelLoader:

    @staticmethod
    def load(file_path: str):

        return pd.read_excel(file_path)