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

def check_plagiarism(given_pdf, local_pdfs):
    given_text = extract_text_from_pdf(given_pdf)

    total_similarity = 0
    for local_pdf in local_pdfs:
        local_text = extract_text_from_pdf(local_pdf)
        similarity = compare_texts(given_text, local_text)
        st.write(f'{local_pdf.name}: {similarity * 100}%')
        total_similarity += similarity

    overall_plagiarism = (total_similarity / len(local_pdfs)) * 100
    st.write(f'\nOverall Plagiarism: {overall_plagiarism}%')

# Streamlit app
st.title('Plagiarism Checker')

# GUI for selecting the given PDF file
given_pdf = st.file_uploader('Select Given PDF File', type='pdf')

# GUI for selecting the local PDF files
local_pdfs = st.file_uploader('Select Local PDF Files', type='pdf', accept_multiple_files=True)

if st.button('Check Plagiarism'):
    if given_pdf is not None and local_pdfs is not None:
        check_plagiarism(given_pdf, local_pdfs)
    else:
        st.warning('Please select the given PDF file and the local PDF files.')
