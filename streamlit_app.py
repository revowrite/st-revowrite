import streamlit as st
import pip

def install_dependencies():
    required_packages = [
        'streamlit',
        'language-tool-python'
    ]

    st.write("Installing dependencies...")
    st.empty()
    st.info("This may take a few moments.")

    for package in required_packages:
        pip.main(['install', package])

    st.success("Dependencies installed successfully.")

def correct_grammar(text):
    import language_tool_python
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_tool_python.correct(text, matches)
    return corrected_text

def main():
    install_dependencies()

    st.title("Grammar Checker")
    st.write("Enter text and click the 'Check Grammar' button to correct grammar mistakes.")

    text = st.text_area("Enter text", height=200)
    if st.button("Check Grammar"):
        corrected_text = correct_grammar(text)
        st.subheader("Corrected Text")
        st.write(corrected_text)

if __name__ == "__main__":
    main()
