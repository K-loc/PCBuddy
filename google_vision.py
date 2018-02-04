import io
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
from pathlib import Path

credentials = service_account.Credentials.from_service_account_file('C:\\Users\\Kevin\\Desktop\\PCBuddy\\Detect Computer Parts-bfacd847a6aa.json')
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])

# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=scoped_credentials)

def detect_part(file_path: Path):
    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    computer_parts = ['motherboard', 'sound card', 'cpu', 'video card', 'power supply', 'random access memory', 'hard disk drive',
                  'computer case', 'optical disk drive']

    result_formatted = ''
    for label in labels:
        if label.description in computer_parts:
            result = label.description
            result_formatted = result.replace(' ', '_')


    return result_formatted

