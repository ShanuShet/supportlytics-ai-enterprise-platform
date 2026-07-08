from backend.ingestion.csv_loader import CSVLoader
from backend.ingestion.excel_loader import ExcelLoader
from backend.ingestion.json_loader import JSONLoader

from backend.ingestion.validator import DatasetValidator
from backend.ingestion.cleaner import DataCleaner
from backend.ingestion.transformer import DataTransformer
from backend.ingestion.duplicate_detector import DuplicateDetector
from backend.ingestion.feature_engineering import FeatureEngineering


class IngestionService:

    @staticmethod
    def ingest(file_path: str):

        if file_path.endswith(".csv"):

            df = CSVLoader.load(file_path)

        elif file_path.endswith(".xlsx"):

            df = ExcelLoader.load(file_path)

        elif file_path.endswith(".json"):

            df = JSONLoader.load(file_path)

        else:

            raise ValueError("Unsupported file type")

        validation = DatasetValidator.validate(df)

        if not validation["valid"]:

            return validation

        df = DataCleaner.clean(df)

        df = DuplicateDetector.remove(df)

        df = DataTransformer.transform(df)

        df = FeatureEngineering.generate(df)

        return {

            "status": "success",

            "rows": len(df),

            "columns": list(df.columns),

            "data": df

        }