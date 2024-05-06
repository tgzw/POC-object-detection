
## Deployment



### Locally
Download a RetinaNet model (like https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth/) and put it in `object_detection/assets/models`
Use python 3.11.0
```
pip install -r requirements
```
```
python -m uvicorn --host 0.0.0.0 --port 8000 object_detection.app:app
```

### In docker
```
docker compose up -d
```

## Endpoints

### object_recognition (POST)
Receives a jpg file and returns a json of the form:
```
{
    "people": [
        {"name": "person",
        "percentage_probability": 100.00,
        "box_points": [0, 0, 0, 0]
        }, 
        ...
    ],
    "cars": [
        {"name": "car",
        "percentage_probability": 100.00,
        "box_points": [0, 0, 0, 0]
        }, 
        ...
    ]
}
```

## Considerations
- The project doesn't have loggins