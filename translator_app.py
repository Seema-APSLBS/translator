import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Multi-Language Translation Tool")

# Input text
input_text = st.text_area("Enter text to translate:", "")

# Language selection
available_languages = [
    "es", "fr", "de", "hi", "zh-cn", "ar", "ru", "ja", "pt"
]

selected_languages = st.multiselect(
    "Select target languages:",
    options=available_languages,
    default=["es", "fr", "de"]
)

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        st.subheader("Translations:")
        for lang in selected_languages:
            translated = GoogleTranslator(source="auto", target=lang).translate(input_text)
            st.write(f"**{lang}**: {translated}")


