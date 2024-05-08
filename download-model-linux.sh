#!/bin/bash

url="https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth"
outputDirectory="object_detection/assets/models"

# Check if the file exists
if [ ! -f "$outputDirectory/retinanet_resnet50_fpn_coco-eeacb38b.pth" ]; then
    # Check if the output directory exists, if not, create it
    mkdir -p "$outputDirectory"
    
    # Download the file
    wget -O "$outputDirectory/retinanet_resnet50_fpn_coco-eeacb38b.pth" "$url"
    
    echo "File downloaded successfully."
else
    echo "File already exists. Skipping download."
fi

