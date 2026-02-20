import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Streamlit app layout
st.title("🌍 Multi-Language Translation Tool")

# Input text
input_text = st.text_area("Enter text to translate:", "")

# Language selection (ISO codes)
available_languages = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-cn",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Portuguese": "pt"
}

selected_languages = st.multiselect(
    "Select target languages:",
    options=list(available_languages.keys()),
    default=["Spanish", "French", "German"]
)

# Translate button
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        st.subheader("Translations:")
        for lang in selected_languages:
            lang_code = available_languages[lang]
            translated = translator.translate(input_text, dest=lang_code)
            st.write(f"**{lang}**: {translated.text}")
