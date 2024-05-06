FROM python:3.11.0

COPY . /app
WORKDIR /app

# Download model
RUN curl -LJO https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth/
RUN cp retinanet_resnet50_fpn_coco-eeacb38b.pth /app/object_detection/assets/models/

# Install system dependencies
RUN apt-get update -y \
    && apt-get install -y libgl1 ghostscript python3-tk \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
RUN pip install -r requirements.txt

# Run
CMD python -m uvicorn --host 0.0.0.0 --port 8000 object_detection.app:app