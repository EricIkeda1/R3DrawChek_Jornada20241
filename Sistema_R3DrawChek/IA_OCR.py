import cv2
import pytesseract
from PIL import Image
import numpy as np


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.medianBlur(gray_image, 3)

    threshold_image = cv2.adaptiveThreshold(blurred_image, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    preprocessed_image_path = 'preprocessed_image.png'
    cv2.imwrite(preprocessed_image_path, threshold_image)

    return preprocessed_image_path

def perform_ocr(image_path, lang='por'):

    preprocessed_image_path = preprocess_image(image_path)

    image = Image.open(preprocessed_image_path)

    text = pytesseract.image_to_string(image, lang=lang)

    return text

if __name__ == "__main__":

    image_path = ' '

    recognized_text = perform_ocr(image_path, lang='por')

    print("Texto reconhecido:")
    print(recognized_text)
