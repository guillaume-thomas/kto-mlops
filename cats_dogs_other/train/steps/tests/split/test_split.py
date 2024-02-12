import os
import shutil
import unittest
from pathlib import Path

from cats_dogs_other.train.steps.s3_wrapper import IS3ClientWrapper
from cats_dogs_other.train.steps.split import random_split_train_evaluate_test_from_extraction

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input/images"

output_directory_train = output_directory / "train"
output_directory_evaluate = output_directory / "evaluate"
output_directory_test = output_directory / "test"

extract = {
    "a_page0_index0.png": "other",
    "a_page1_index0.png": "other",
    "a_page2_index0.png": "other",
    "b_page1_index0.png": "cat",
    "b_page2_index0.png": "dog",
    "b_page3_index0.png": "cat",
    "b_page4_index0.png": "dog",
    "c_page4_index0.png": "dog",
    "d_page0_index0.png": "other"
}
classes = {"cat", "dog", "other"}


class TestS3ClientWrapper(IS3ClientWrapper):

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        Path(dest_filename).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(s3_path, dest_filename)


class SplitTest(unittest.TestCase):
    def test_splitting_works_properly(self):
        random_split_train_evaluate_test_from_extraction(extract, classes, 0.55, 0.3, 0.15,
                                                         str(output_directory_train), str(output_directory_evaluate),
                                                         str(output_directory_test), "bucket",
                                                         str(input_directory) + "/", TestS3ClientWrapper())
        self.count_files_in_directory_and_assert(output_directory_train, 4)
        self.count_files_in_directory_and_assert(output_directory_evaluate, 3)
        self.count_files_in_directory_and_assert(output_directory_test, 2)
        shutil.rmtree(str(output_directory))

    def count_files_in_directory_and_assert(self, dir_path: Path, count_asserted: int):
        total = 0
        for root, dirs, files in os.walk(dir_path):
            total += len(files)
        self.assertEqual(total, count_asserted)

    def test_splitting_with_ratios_not_equal_to_one_raises_an_exception(self):
        self.assertRaises(Exception, random_split_train_evaluate_test_from_extraction, extract, classes, 0.25, 0.3,
                          0.15, str(output_directory_train), str(output_directory_evaluate), str(output_directory_test),
                          "bucket", str(input_directory) + "/", TestS3ClientWrapper())
        

if __name__ == '__main__':
    unittest.main()
