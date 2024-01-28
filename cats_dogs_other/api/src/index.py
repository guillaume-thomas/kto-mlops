import io
import logging
import os 

from fastapi import FastAPI, UploadFile, Depends 
from fastapi.security import OAuth2PasswordBearer 
from kto.inference import Inference
from oidc_jwt_validation.authentication import Authentication 
from oidc_jwt_validation.http_service import ServiceGet 

app = FastAPI()
model = Inference("./cats_dogs_other/api/resources/final_model.keras")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

issuer = os.getenv("OAUTH2_ISSUER") 
audience = os.getenv("OAUTH2_AUDIENCE") 
jwks_uri = os.getenv("OAUTH2_JWKS_URI") 
logger = logging.getLogger(__name__) 
authentication = Authentication(logger, issuer, ServiceGet(logger), jwks_uri) 
skip_oidc = False 


@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/upload")
async def upload(file: UploadFile, token: str = Depends(oauth2_scheme)): 
    if not skip_oidc:
        await authentication.validate_async(token, audience, "get::prediction") 
    file_readed = await file.read()
    file_bytes = io.BytesIO(file_readed)
    return model.execute(file_bytes)