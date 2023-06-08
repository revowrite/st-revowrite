import os
from difflib import SequenceMatcher
from PyPDF2 import PdfFileReader
import streamlit as st

def extract_text_from_pdf(pdf_file):
    pdf = PdfFileReader(pdf_file)
    text = ''
    for page in range(pdf.getNumPages()):
        text += pdf.getPage(page).extractText()
    return text

def compare_texts(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def check_plagiarism(given_pdf, local_folder):
    given_text = extract_text_from_pdf(given_pdf)

    total_similarity = 0
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                with open(pdf_path, 'rb') as file:
                    local_text = extract_text_from_pdf(file)
                    similarity = compare_texts(given_text, local_text)
                    st.write(f'{file}: {similarity * 100}%')
                    total_similarity += similarity

    overall_plagiarism = (total_similarity / len(files)) * 100
    st.write(f'\nOverall Plagiarism: {overall_plagiarism}%')

# Streamlit app
st.title('Plagiarism Checker')

# GUI for selecting the given PDF file
given_pdf = st.file_uploader('Select Given PDF File', type='pdf')

# GUI for selecting the local PDF folder
local_folder = st.folder_uploader('Select Local PDF Folder')

if st.button('Check Plagiarism'):
    if given_pdf is not None and local_folder is not None:
        check_plagiarism(given_pdf, local_folder)
    else:
        st.warning('Please select the given PDF file and the local PDF folder.')
