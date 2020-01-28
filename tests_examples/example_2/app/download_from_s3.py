import datetime

import boto3
from botocore.exceptions import ClientError

from tests_examples.example_2.app.utils import dir_path
from tests_examples.example_2.app.config import settings, logger

s3 = boto3.resource(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)


def download_s3_object(key: str, destination_file: str) -> None:
    s3.Bucket(settings.BUCKET_NAME).download_file(key, destination_file)


def download_file_from_s3() -> None:
    date_today: str = datetime.date.today().strftime(settings.DATE_FORMAT)
    logger.debug(f"Starting the process of day {date_today}")

    key = f"{settings.S3_FOLDER_PREFIX}/{date_today}.txt"
    output_file_path = f"{dir_path}/tmp/mussum-{date_today}.txt"

    try:
        download_s3_object(key, output_file_path)
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            logger.info(f"The file with key {key} was not found")
        else:
            raise


if __name__ == "__main__":
    download_file_from_s3()
