class DataCleaner:

    @staticmethod
    def clean(dataframe):

        dataframe = dataframe.drop_duplicates()

        dataframe = dataframe.fillna("Unknown")

        return dataframe