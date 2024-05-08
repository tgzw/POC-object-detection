
## Deployment



### Locally

#### In Windows
Run `download-model-win.ps1`  
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