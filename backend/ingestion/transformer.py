class DataTransformer:

    @staticmethod
    def transform(dataframe):

        dataframe.columns = [

            column.strip()

            for column in dataframe.columns

        ]

        return dataframe