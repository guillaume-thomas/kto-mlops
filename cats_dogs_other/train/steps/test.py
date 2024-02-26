import json
from pathlib import Path

from kto.inference import Inference


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