import shutil
import unittest
from pathlib import Path

from cats_dogs_other.label.extraction import extract_images

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"


class TestExtraction(unittest.TestCase):

    def test_pdfs_images_should_be_extracted(self):
        if output_directory.is_dir():
            shutil.rmtree(str(output_directory))
        result = extract_images(str(input_directory), str(output_directory))
        expected_number_files_input = 3
        self.assertEqual(expected_number_files_input, result.number_files_input)
        expected_number_images_output = 4
        self.assertEqual(expected_number_images_output, result.number_images_output)
        shutil.rmtree(str(output_directory))


if __name__ == "__main__":
    unittest.main()
