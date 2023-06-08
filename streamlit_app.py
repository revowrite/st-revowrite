import streamlit as st
import re
from spellchecker import SpellChecker

def correct_grammar(text):
    spell = SpellChecker()

    # Tokenize the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Correct the spelling for each sentence
    corrected_sentences = []
    for sentence in sentences:
        words = sentence.split()
        corrected_words = []
        for word in words:
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word)
        corrected_sentence = ' '.join(corrected_words)
        corrected_sentences.append(corrected_sentence)

    # Join the corrected sentences into a single text
    corrected_text = ' '.join(corrected_sentences)

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
