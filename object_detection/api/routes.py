from fastapi import APIRouter, File, UploadFile
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from object_detection.api.response import SuccesfullResponse
import object_detection.api.services as services


detection_routes = APIRouter()


@detection_routes.post("/object_recognition/", response_model=SuccesfullResponse)
async def object_recognition(file: UploadFile = File(...)):
    try:
        response = await services.object_recognition(file)
    except Exception as e:
        raise HTTPException(e)

    return response
