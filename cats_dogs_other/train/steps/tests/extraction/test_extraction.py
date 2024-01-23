import shutil
import unittest
from pathlib import Path

from cats_dogs_other.train.steps.extraction import extraction_from_annotation_file
from cats_dogs_other.train.steps.s3_wrapper import IS3ClientWrapper

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"
expected_extract = {
    "a_page0_index0.png": "other",
    "b_page2_index0.png": "other",
    "b_page4_index0.png": "cat",
    "c_page4_index0.png": "dog"
}


class TestS3ClientWrapper(IS3ClientWrapper):

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        Path(dest_filename).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(s3_path, dest_filename)


class TestExtraction(unittest.TestCase):

    def test_extraction(self):
        extract, classes = extraction_from_annotation_file("bucket", # ce paramètre n'a pas d'importance
                                                           str(input_directory / "labels.json"),
                                                           str(output_directory / "labels.json"),
                                                           TestS3ClientWrapper())
        self.assertEqual(sorted({"cat", "other", "dog"}), sorted(classes))
        self.assertEqual(expected_extract, extract)
        shutil.rmtree(str(output_directory))


if __name__ == "__main__":
    unittest.main()
