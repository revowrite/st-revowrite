import streamlit as st
import csv
import io
import base64

def generate_csv_file():
    # Create a CSV file in memory
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)

    # Write the header row
    writer.writerow(['Name of Society', 'Address', 'State', 'District', 'Date of Registration', 'Area of Operation', 'Sector Type'])

    # Write the data row
    writer.writerow([name_input, address_input, state_input, district_input, registration_input, operation_input, sector_input])

    # Retrieve the value from the buffer
    csv_buffer.seek(0)
    csv_data = csv_buffer.getvalue()
    csv_buffer.close()

    # Create a download link for the CSV file
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:text/csv;base64,{b64}" download="society_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)

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

# Create a home button to redirect to another website
import streamlit as st

# Create a home button to redirect to another website
if st.button("Home"):
    st.markdown(
        """
        <script>
            window.open('https://techcodebhavesh.github.io/crcba/#hero', '_blank');
        </script>
        """,
        unsafe_allow_html=True
    )



