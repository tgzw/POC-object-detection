from object_detection.modules.objects_recognition import detector
from object_detection.config import cache_path
from object_detection.modules.logger import getLogger
from object_detection.api.response import SuccesfullResponse

import json
import os
import aiofiles


logger = getLogger(__name__)


async def object_recognition(file):
    logger.info("file in service")
    async with aiofiles.open(os.path.join(cache_path, "temp.jpg"), "wb") as hf:
        content = await file.read()
        await hf.write(content)
    # with open(os.path.join(cache_path, "temp.jpg"), "wb") as hf:
    #     hf.write(file)
    detections = detector.detectObjectsFromImage(
        input_image=os.path.join(cache_path, "temp.jpg"),
        output_image_path=os.path.join(cache_path, "output_temp.jpg"),
        minimum_percentage_probability=30,
    )

    return response_formater(detections)


def response_formater(detections):
    person_detections = [item for item in detections if item["name"] == "person"]
    car_detections = [item for item in detections if item["name"] == "car"]

    response = {"people": person_detections, "cars": car_detections}

    response = SuccesfullResponse(people=person_detections, cars=car_detections)

    return response  # json.dumps(response) # json.dumps(json.JSONDecoder().decode(json.dumps(response)))
