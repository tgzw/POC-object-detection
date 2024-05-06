from object_detection.config import models_path

from imageai.Detection import ObjectDetection
import os


detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(models_path, os.getenv("RECOGNITION_MODEL")))
detector.loadModel()
