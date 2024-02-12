import shutil
import unittest
from pathlib import Path

from cats_dogs_other.train.steps.train_and_evaluate import train_and_evaluate_model

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"
train_directory = input_directory / "train"
evaluate_directory = input_directory / "evaluate"
test_directory = input_directory / "test"
model_path = output_directory / "model.h5"
model_plot_path = output_directory / "model_plot.png"


class TrainTest(unittest.TestCase):
    def test_train(self):
        if output_directory.is_dir():
            shutil.rmtree(str(output_directory))
        train_and_evaluate_model(str(train_directory), str(evaluate_directory), str(test_directory),
                                 str(output_directory),
                                 str(model_path),
                                 str(model_plot_path),
                                 10, 1)
        self.assertEqual(True, model_path.is_file())
        self.assertEqual(True, model_plot_path.is_file())
        shutil.rmtree(str(output_directory))


if __name__ == '__main__':
    unittest.main()
