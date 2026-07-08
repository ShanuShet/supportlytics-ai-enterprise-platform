import pandas as pd


class FeatureStore:

    @staticmethod
    def build_features(df: pd.DataFrame):

        dataframe = df.copy()

        if "created_date" in dataframe.columns:

            dataframe["created_date"] = pd.to_datetime(
                dataframe["created_date"],
                errors="coerce"
            )

            dataframe["year"] = dataframe["created_date"].dt.year

            dataframe["month"] = dataframe["created_date"].dt.month

            dataframe["weekday"] = dataframe["created_date"].dt.day_name()

        return dataframe