import os
import unittest
from unittest.mock import patch

from tests_examples.example_1.file_operations import group_content, remove

PATH = os.path.dirname(os.path.abspath(__file__))


class TestGroupContent(unittest.TestCase):
    def setUp(self) -> None:
        self.file_names = [
            f"{PATH}/fixtures/fruit_list_en.txt",
            f"{PATH}/fixtures/fruit_list_pt.txt",
        ]

    def test_if_returns_all_the_content_of_files_grouped_in_a_structure(self):
        result = group_content(files=self.file_names)
        expected = [
            "apple",
            "orange",
            "banana",
            "grapefruit",
            "lemon",
            "peach",
            "maçã",
            "laranja",
            "banana",
            "toranja",
            "limão",
            "pêssego",
        ]

        self.assertEqual(result, expected)

    def test_if_returns_an_empty_list_when_there_is_not_content_in_file(self):
        result = group_content(files=[f"{PATH}/fixtures/empty_file.txt"])
        expected = []
        self.assertListEqual(result, expected)


class TestRemove(unittest.TestCase):
    def test_if_remove_all_files_received(self):
        with patch.object(os, "remove") as remove_mock:
            remove(files=["rio.txt", "tokyo.txt", "professor.txt"])

            remove_mock.assert_called()
            self.assertEqual(remove_mock.call_count, 3)
