import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Example Project"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
