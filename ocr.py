import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    try:
        print("OCR IMAGE PATH:", image_path)

        img = cv2.imread(image_path)

        if img is None:
            print("Image not readable:", image_path)
            return ""

        img = cv2.resize(img, None, fx=2, fy=2)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        text = pytesseract.image_to_string(
            thresh,
            config="--oem 3 --psm 6"
        )

        print("OCR OUTPUT:")
        print(text)

        return text.strip()

    except Exception as e:
        print("OCR Error:", e)
        return ""