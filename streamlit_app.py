import streamlit as st
import cv2
import pytesseract
from PIL import Image
import io

# Set up the Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Define a function to perform OCR on the selected image and display the result
def perform_ocr(file_bytes):
    # Open the image from the uploaded file bytes
    img = Image.open(io.BytesIO(file_bytes))

    # Convert the image to grayscale and perform OCR
    img = img.convert('L')
    text = pytesseract.image_to_string(img)

    # Display the OCR result
    st.write("OCR Result:")
    st.write(text)

def main():
    st.title("Image OCR")

    # Display a file uploader widget
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the file bytes and perform OCR
        image_bytes = uploaded_file.read()
        perform_ocr(image_bytes)

if _name_ == '_main_':
    main()

#streamlit run front.py
