import argparse
import os
import boto3

from steps.extraction import extraction_from_annotation_file
from steps.split import random_split_train_evaluate_test_from_extraction
from steps.test import Inference, test_model
from steps.train_and_evaluate import train_and_evaluate_model

parser = argparse.ArgumentParser("training")
parser.add_argument("--split_ratio_train", type=float)
parser.add_argument("--split_ratio_evaluate", type=float)
parser.add_argument("--split_ratio_test", type=float)
parser.add_argument("--batch_size", type=int)
parser.add_argument("--epochs", type=int)
parser.add_argument("--working_dir", type=str)

args = parser.parse_args()
split_ratio_train = args.split_ratio_train
split_ratio_evaluate = args.split_ratio_evaluate
split_ratio_test = args.split_ratio_test
batch_size = args.batch_size
epochs = args.epochs
working_dir = args.working_dir

if __name__ == "__main__":
  s3_client = boto3.client(
    "s3",
    endpoint_url=os.environ.get("MLFLOW_S3_ENDPOINT_URL"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
  )

  bucket_name = "cats-dogs-other"
  extract, classes = extraction_from_annotation_file(bucket_name,
                                                     "dataset/cats_dogs_others-annotations.json",
                                                     working_dir + "/cats_dogs_others-annotations.json",
                                                     s3_client)

  train_dir = working_dir + "/train"
  evaluate_dir = working_dir + "/evaluate"
  test_dir = working_dir + "/test"

  random_split_train_evaluate_test_from_extraction(extract, classes, split_ratio_train,
                                                   split_ratio_evaluate, split_ratio_test,
                                                   train_dir, evaluate_dir, test_dir, bucket_name,
                                                   "dataset/extract/", s3_client)

  model_filename = "final_model.h5"
  model_plot_filename = "model_plot.png"

  # train & evaluate
  model_dir = working_dir + "/model"
  model_path = model_dir + "/" + model_filename
  plot_filepath = model_dir + "/" + model_plot_filename

  train_and_evaluate_model(train_dir, evaluate_dir, test_dir, model_dir, model_path,
                           plot_filepath, batch_size, epochs)

  # test the model
  model_inference = Inference(model_path)

  test_model(model_inference, model_dir, test_dir)
