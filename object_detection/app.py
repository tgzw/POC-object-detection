from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from object_detection.api.routes import detection_routes


app = FastAPI()

app.include_router(detection_routes)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3003)
