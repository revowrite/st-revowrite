import streamlit as st
import requests

def correct_grammar(text):
    url = "https://api.grammarbot.io/v2/check"
    params = {
        "text": text,
        "language": "en-US"
    }
    response = requests.post(url, json=params)
    result = response.json()
    
    corrected_text = text
    matches = result.get("matches")
    if matches:
        for match in matches:
            replacement = match["replacements"][0]["value"]
            incorrect = match["context"]["text"]
            corrected_text = corrected_text.replace(incorrect, replacement)
    
    return corrected_text

def main():
    st.title("Grammar Checker")
    st.write("Enter text and click the 'Check Grammar' button to correct grammar mistakes.")

    text = st.text_area("Enter text", height=200)
    if st.button("Check Grammar"):
        corrected_text = correct_grammar(text)
        st.subheader("Corrected Text")
        st.write(corrected_text)

if __name__ == "__main__":
    main()
