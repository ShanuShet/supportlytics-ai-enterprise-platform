import os

class Config:

    APP_NAME = "Supportlytics AI"

    VERSION = "2.0.0"

    DEBUG = True

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./supportlytics.db"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "supportlytics_secret_key"
    )