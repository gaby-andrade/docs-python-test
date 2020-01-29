import datetime
from unittest import TestCase
from unittest.mock import patch

from botocore.exceptions import ClientError
from freezegun import freeze_time

from tests_examples.example_3.app.config import settings
from tests_examples.example_3.app.download_from_s3 import download_file_from_s3
from tests_examples.example_3.app.utils import dir_path


@freeze_time("2020-01-27")
class DownloadObjectTest(TestCase):
    def setUp(self):
        self.date_today = datetime.date.today()
        self.key_to_download = f"{settings.S3_FOLDER_PREFIX}/{self.date_today}.txt"
        self.log_mock = patch(
            "tests_examples.example_3.app.download_from_s3.logger.exception"
        ).start()

    def test_it_download_is_successful(self):

        file_name = f"{dir_path}/tmp/mussum-{self.date_today}.txt"
        with patch("tests_examples.example_3.app.download_from_s3.s3") as download_mock:

            download_file_from_s3()

            download_mock.Bucket.assert_called_with(settings.BUCKET_NAME)
            download_mock.Bucket().download_file.assert_called_with(
                self.key_to_download, file_name
            )

    def test_it_logs_when_object_to_download_is_not_found(self):
        with patch(
            "tests_examples.example_3.app.download_from_s3.download_s3_object",
            side_effect=ClientError(
                {"Error": {"Code": "404", "Message": "Not Found"}}, "operacao"
            ),
        ):

            download_file_from_s3()
            self.log_mock.assert_called_once_with(
                "The file with key mussumipsum/2020-01-27.txt was not found"
            )

    def test_it_raises_exception_if_another_error_with_code_differently_from_not_found_happens(self):
        with patch(
            "tests_examples.example_3.app.download_from_s3.download_s3_object",
            side_effect=ClientError(
                {"Error": {"Code": "500", "Message": "Internal Error"}}, "operacao"
            ),
        ):

            with self.assertRaises(ClientError):
                download_file_from_s3()
