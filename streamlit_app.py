import streamlit as st
import csv
import base64

def generate_csv_file():
    society_data = {
        'Name of Society': name_input,
        'Address': address_input,
        'State': state_input,
        'District': district_input,
        'Date of Registration': registration_input,
        'Area of Operation': operation_input,
        'Sector Type': sector_input
    }
    
    fieldnames = ['Name of Society', 'Address', 'State', 'District', 'Date of Registration', 'Area of Operation', 'Sector Type']

    with open('society_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(society_data)
    
    # Set the submitted flag to True
    st.session_state.submitted = True

# Create the form inputs
name_input = st.text_input("Name of Society")
address_input = st.text_input("Address")
state_input = st.text_input("State")
district_input = st.text_input("District")
registration_input = st.date_input("Date of Registration")
operation_input = st.text_input("Area of Operation")
sector_input = st.text_input("Sector Type")

# Create the submit button
if st.button("Submit"):
    generate_csv_file()

# Optionally, you can add a success message after the submission
if 'submitted' in st.session_state and st.session_state.submitted:
    st.write("CSV File Generated", "Click the button below to download the CSV file.")
    csv_file = open('society_data.csv', 'r').read()
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="society_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
