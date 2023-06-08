import streamlit as st
import spacy

def correct_grammar(text):
    # Load the English language model in spaCy
    nlp = spacy.load('en_core_web_sm')

    # Process the text with spaCy
    doc = nlp(text)

    # Implement your grammar correction logic using spaCy's syntactic analysis

    # Example rule: Correct "is not" to "isn't"
    for token in doc:
        if token.text == "is" and token.idx > 0 and doc[token.i-1].text.lower() == "not":
            corrected_text = doc.text[:token.idx-1] + "n't" + doc.text[token.idx+len(token):]
            doc = nlp(corrected_text)

    corrected_text = doc.text

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
