import io
from fastapi import FastAPI, UploadFile
from kto.inference import Inference

app = FastAPI()
model = Inference("./cats_dogs_other/api/resources/final_model.keras")


@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/upload")
async def upload(file: UploadFile):
    file_readed = await file.read()
    file_bytes = io.BytesIO(file_readed)
    return model.execute(file_bytes)