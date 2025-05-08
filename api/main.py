from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import random

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    classes = ["cat", "dog", "other"]
    prediction = random.choice(classes)

    return JSONResponse(content={
        "prediction": prediction,
        "filename": file.filename
    })
