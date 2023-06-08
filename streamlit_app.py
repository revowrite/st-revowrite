import streamlit as st
import pipreqs

def install_dependencies():
    required_packages = ['streamlit', 'language-tool-python']
    pipreqs_path = '/tmp/requirements.txt'

    # Generate requirements.txt file
    pipreqs.generate('.', pipreqs_path, encoding='utf-8')

    # Install required packages using pip
    st.write("Installing dependencies...")
    st.empty()
    st.info("This may take a few moments.")

    cmd = ['pip', 'install', '-r', pipreqs_path]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        st.error("Failed to install dependencies.")
        st.code(stderr.decode('utf-8'))
    else:
        st.success("Dependencies installed successfully.")
        st.code(stdout.decode('utf-8'))

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
