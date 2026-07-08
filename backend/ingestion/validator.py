class DatasetValidator:

    REQUIRED_COLUMNS = [
        "Ticket ID",
        "Category",
        "Priority"
    ]

    @classmethod
    def validate(cls, dataframe):

        missing = []

        for column in cls.REQUIRED_COLUMNS:

            if column not in dataframe.columns:
                missing.append(column)

        return {

            "valid": len(missing) == 0,

            "missing_columns": missing

        }