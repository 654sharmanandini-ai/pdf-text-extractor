import cv2
import numpy as np
import pytesseract
from PIL import Image


def preprocess_image(image):
    # PIL → numpy conversion
    if isinstance(image, Image.Image):
        image = np.array(image)

    # ensure valid numpy array
    if image is None or not isinstance(image, np.ndarray):
        return None

    # grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise remove
    gray = cv2.medianBlur(gray, 3)

    # threshold
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return thresh


def extract_text_from_images(images):
    text = ""

    for img in images:
        processed = preprocess_image(img)

        if processed is None:
            continue

        extracted = pytesseract.image_to_string(
            processed,
            config="--oem 3 --psm 6"
        )

        text += extracted + "\n"

    return text
