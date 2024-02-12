import json
from io import BytesIO
from pathlib import Path

import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array


# load and prepare the image
def load_image(filename: str|BytesIO):
  # load the image
  img = load_img(filename, target_size=(224, 224))
  # convert to array
  img = img_to_array(img)
  # reshape into a single sample with 3 channels
  img = img.reshape(1, 224, 224, 3)
  # center pixel data
  img = img.astype('float32')
  img = img - [123.68, 116.779, 103.939]
  return img


class Inference:
  def __init__(self, model_path: str):
    self.model = load_model(model_path)

  def execute(self, filepath:str|BytesIO):
    img = load_image(filepath)
    result = self.model.predict(img)
    values = [float(result[0][0]), float(result[0][1]), float(result[0][2])]
    switcher = ['Cat', 'Dog', 'Other']
    prediction = np.argmax(result[0])
    return {"prediction": switcher[prediction], "values": values}


def test_model(model_inference: Inference, model_dir: str, test_dir: str):
  statistics = {"ok": 0, "ko": 0, "total": 0}
  results = []
  path_test_dir = Path(test_dir)
  for path in path_test_dir.glob("**/*"):
    if path.is_dir():
      continue
    model_result = model_inference.execute(str(path))

    prediction = model_result["prediction"]
    prediction_truth = path.parent.name.lower().replace("s", "")
    status = prediction_truth == prediction.lower()
    statistics["ok" if status else "ko"] += 1
    result = {
      "filename": path.name,
      "ok": status,
      "prediction": prediction,
      "prediction_truth": prediction_truth,
      "values": model_result["values"],
    }
    results.append(result)
  statistics["total"] = statistics["ok"] + statistics["ko"]

  with open(model_dir + "/statistics.json", "w") as file_stream:
    json.dump(statistics, file_stream, indent=4)

  with open(model_dir + "/predictions.json", "w") as file_stream:
    json.dump(results, file_stream, indent=4)
