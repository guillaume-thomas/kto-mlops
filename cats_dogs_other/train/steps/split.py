import random
from pathlib import Path

import mlflow.keras

from .s3_wrapper import IS3ClientWrapper


def random_split_train_evaluate_test_from_extraction(extract: dict,
                                                     classes: set,
                                                     split_ratio_train: float,
                                                     split_ratio_evaluate: float,
                                                     split_ratio_test: float,
                                                     train_dir: str,
                                                     evaluate_dir: str,
                                                     test_dir: str,
                                                     bucket_name: str,
                                                     s3_path: str,
                                                     s3_client: IS3ClientWrapper):
    if split_ratio_train + split_ratio_evaluate + split_ratio_test != 1:
        raise Exception("sum of ratio must be equal to 1")

    keys_list = list(extract.keys())  # shuffle() wants a list
    random.shuffle(keys_list)  # randomize the order of the keys

    nkeys_train = int(split_ratio_train * len(keys_list))  # how many keys does split ratio train% equal
    keys_train = keys_list[:nkeys_train]
    keys_evaluate_and_test = keys_list[nkeys_train:]

    split_ratio_evaluate_and_test = split_ratio_evaluate + split_ratio_test
    nkeys_evaluate = int((split_ratio_evaluate / split_ratio_evaluate_and_test) * len(keys_evaluate_and_test))
    keys_evaluate = keys_evaluate_and_test[:nkeys_evaluate]
    keys_test = keys_evaluate_and_test[nkeys_evaluate:]

    extract_train = {k: extract[k] for k in keys_train}
    extract_evaluate = {k: extract[k] for k in keys_evaluate}
    extract_test = {k: extract[k] for k in keys_test}

    # create directories
    for existing_class in classes:
        Path(train_dir + "/" + existing_class).mkdir(parents=True, exist_ok=True)
        Path(evaluate_dir + "/" + existing_class).mkdir(parents=True, exist_ok=True)
        Path(test_dir + "/" + existing_class).mkdir(parents=True, exist_ok=True)

    # add files in directories
    download_files(extract_train, train_dir, bucket_name, s3_path, s3_client)
    download_files(extract_evaluate, evaluate_dir, bucket_name, s3_path, s3_client)
    download_files(extract_test, test_dir, bucket_name, s3_path, s3_client)

    mlflow.log_dict(extract_train, "annotations/split_train.json")
    mlflow.log_dict(extract_evaluate, "annotations/split_evaluate.json")
    mlflow.log_dict(extract_test, "annotations/split_test.json")


def download_files(extract: dict, directory: str, bucket_name: str, s3_path: str, s3_client: IS3ClientWrapper):
    for key, value in extract.items():
        s3_client.download_file(bucket_name, s3_path + key, directory + "/" + value + "/" + key)
