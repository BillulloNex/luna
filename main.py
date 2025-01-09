import time
import subprocess
import google.generativeai as genai
import dotenv
dotenv.load_dotenv()
import os
import httpx
import base64
import PIL.Image

GOOGLE_GEMINI_API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)


import cv2

def capture_image(filename="captured_image.jpg"):
    camera = cv2.VideoCapture(1)
    ret, frame = camera.read()
    camera.release()
    if ret:
        cv2.imwrite(filename, frame)
        return True
    return False


def caption_image():
    model = genai.GenerativeModel(model_name = "gemini-1.5-flash")

    while True:
        if capture_image():
            image_path = 'captured_image.jpg'
            image = PIL.Image.open(image_path)

            prompt = "Describe the sentimental and subject in 5 words or less."
            response = model.generate_content([prompt, image])
            print(response.text)
        time.sleep(2)

caption_image()