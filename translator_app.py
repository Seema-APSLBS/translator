import streamlit as st
from deep_translator import GoogleTranslator

st.title("Translator App")
st.write("Translate text between languages using Google Translator (demo).")

# Input text
text = st.text_area("Enter text to translate")

# Select source and target languages
source_lang = st.text_input("Source language (e.g., 'en' for English)", "en")
target_lang = st.text_input("Target language (e.g., 'hi' for Hindi)", "hi")

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            st.success(f"Translated Text:\n{translated}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to translate.")
