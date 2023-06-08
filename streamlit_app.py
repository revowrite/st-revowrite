import os
from difflib import SequenceMatcher
from PyPDF2 import PdfReader
import streamlit as st

def extract_text_from_pdf(pdf_path):
    pdf = PdfReader(pdf_path)
    text = ''
    for page in range(len(pdf.pages)):
        text += pdf.pages[page].extract_text()
    return text

def compare_texts(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def check_plagiarism(given_pdf_folder, local_pdf_folder):
    given_pdfs = os.listdir(given_pdf_folder)
    local_pdfs = os.listdir(local_pdf_folder)

    for given_pdf in given_pdfs:
        given_pdf_path = os.path.join(given_pdf_folder, given_pdf)
        given_text = extract_text_from_pdf(given_pdf_path)

        total_similarity = 0
        for local_pdf in local_pdfs:
            local_pdf_path = os.path.join(local_pdf_folder, local_pdf)
            local_text = extract_text_from_pdf(local_pdf_path)
            similarity = compare_texts(given_text, local_text)
            st.write(f'{local_pdf}: {similarity * 100}%')
            total_similarity += similarity

        overall_plagiarism = (total_similarity / len(local_pdfs)) * 100
        st.write(f'\nOverall Plagiarism for {given_pdf}: {overall_plagiarism}%')

# Streamlit app
st.header('Plagiarism Checker')

# GUI for selecting the given PDF folder
given_pdf_folder = st.text_input('Enter Given PDF Folder Path')

# GUI for selecting the local PDF folder
local_pdf_folder = st.text_input('Enter Local PDF Folder Path')

if st.button('Check Plagiarism'):
    if given_pdf_folder and local_pdf_folder:
        check_plagiarism(given_pdf_folder, local_pdf_folder)
    else:
        st.warning('Please enter both the Given PDF folder path and the Local PDF folder path.')
