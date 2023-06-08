import streamlit as st
import re

def correct_grammar(text):
    # Define your grammar rules here
    rules = [
        (r'\b(i)\b', 'I'),
        (r'\b([a-z])\.', lambda match: match.group(1).upper() + '.'),
        # Add more rules as needed
    ]

    # Apply the grammar rules to the text
    corrected_text = text
    for pattern, repl in rules:
        corrected_text = re.sub(pattern, repl, corrected_text)

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
