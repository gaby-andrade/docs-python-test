import logging

from pydantic import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    BUCKET_NAME: str = "python-test-example-s3"
    S3_FOLDER_PREFIX: str = "mussumipsum"
    DATE_FORMAT: str = "%Y-%m-%d"

    class Config:
        env_prefix = "APP_"


settings = Settings()

logging.basicConfig()
logger = logging.getLogger("example_2")
logger.setLevel(logging.DEBUG)
