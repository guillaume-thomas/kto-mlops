import json
from pathlib import Path
from typing import Any


def extraction_from_annotation_file(bucket_name: str, s3_path: str, filename: str, s3_client) -> tuple[dict[Any, Any], set[Any]]:
  Path(filename).parent.mkdir(parents=True, exist_ok=True)
  s3_client.download_file(bucket_name, s3_path, filename)

  extract = {}
  classes = set()
  with open(filename) as file:
    annotations = json.load(file)["annotations"]
    for annotation in annotations:
      label = annotation["annotation"]["label"]
      extract[annotation["fileName"]] = label
      classes.add(label)
  return extract, classes
