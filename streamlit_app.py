import streamlit as st
from languagetool import LanguageTool

def correct_grammar(text):
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = LanguageTool.correct(text, matches)
    return corrected_text

def main():
    st.title("Grammar Checker")
    st.write("Enter text and click the 'Check Grammar' button to correct grammar mistakes.")

    text = st.text_area("Enter text", height=200)
    if st.button("Check Grammar"):
        try:
            corrected_text = correct_grammar(text)
            st.subheader("Corrected Text")
            st.write(corrected_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
