FROM python:3.11.0

COPY . /app
WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y wget
RUN apt-get update && \
    apt-get install -y \
    wget \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Download model
RUN chmod +x download-model-linux.sh
RUN ./download-model-linux.sh

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run
CMD python -m uvicorn --host 0.0.0.0 --port 8000 object_detection.app:app