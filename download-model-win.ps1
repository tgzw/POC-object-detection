param(
    [string]$url = "https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth",
    [string]$outputDirectory = "object_detection/assets/models/"
)

try {
    # Download the file
    Invoke-WebRequest -Uri $url -OutFile "$outputDirectory\retinanet_resnet50_fpn_coco-eeacb38b.pth"
    Write-Host "File downloaded successfully."
} catch {
    Write-Host "Error downloading the file: $_.Exception.Message"
}