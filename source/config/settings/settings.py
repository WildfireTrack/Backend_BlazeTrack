import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "BlazeTrack"
    PROJECT_DESCRIPTION: str = "Production ready BlazeTrack"
    PROJECT_VERSION: str = "0.1.0"

    API_V1_STR: str = "/api/v1"

    ALLOWED_ORIGINS: list[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")
    ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS", "true").lower() == "true"
    ALLOW_METHODS: list[str] = os.getenv("ALLOW_METHODS", "*").split(",")
    ALLOW_HEADERS: list[str] = os.getenv("ALLOW_HEADERS", "*").split(",")

    MAP_KEY: str = os.getenv("MAP_KEY", "")


settings = Settings()
