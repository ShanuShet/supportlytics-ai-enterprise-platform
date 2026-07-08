import pandas as pd


class FeatureEngineering:

    @staticmethod
    def generate(dataframe):

        if "Created Date" in dataframe.columns:

            dataframe["Created Date"] = pd.to_datetime(
                dataframe["Created Date"],
                errors="coerce"
            )

            dataframe["Year"] = dataframe["Created Date"].dt.year
            dataframe["Month"] = dataframe["Created Date"].dt.month
            dataframe["Day"] = dataframe["Created Date"].dt.day
            dataframe["Weekday"] = dataframe["Created Date"].dt.day_name()

        return dataframe