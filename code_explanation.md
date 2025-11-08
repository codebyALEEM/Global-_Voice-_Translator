# 📘 Global Voice Translator — Code Explanation

This document explains the **Streamlit-based multilingual translator** code line-by-line.

---

## 🧩 1️⃣ Import Libraries

```python
import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64
```
**Explanation:**
- `streamlit`: Creates the web app interface.
- `mtranslate`: Translates text between multiple languages.
- `pandas`: Reads and processes the language CSV file.
- `os`: Manages file paths for saving audio files.
- `gtts`: Converts text into spoken audio using Google Text-to-Speech.
- `base64`: Encodes binary audio data for download links.

---

## 🎨 2️⃣ Custom CSS Styling

This section defines the **look and feel** of the Streamlit app using inline CSS.

```python
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.4),
        rgba(0, 0, 0, 0.4)
    ),
    url("your_image_url_here");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

div[data-baseweb="textarea"], div[data-baseweb="input"] {
    background-color: rgba(255, 255, 255, 0.85);
    color: #000;
    border-radius: 10px;
    padding: 8px;
}

section[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
}

button[kind="primary"] {
    background-color: #008CBA;
    color: white;
    border-radius: 8px;
}
button[kind="primary"]:hover {
    background-color: #005f73;
}
</style>
""", unsafe_allow_html=True)
```
**Explanation:**
- Adds a **background image** with a dark overlay.
- Styles the **text boxes**, **buttons**, and **sidebar**.
- Ensures a **futuristic blue-glow UI**.

---

## 📄 3️⃣ Load and Process Language Data

```python
df = pd.read_csv('language.csv')
df.dropna(inplace=True)
lang = df['name'].to_list()
langcode = df['iso'].to_list()
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}
```
**Explanation:**
- Reads the list of supported languages from a CSV file.
- Cleans missing data (`dropna`).
- Creates a **dictionary** mapping language names to ISO codes.

---

## 🧠 4️⃣ Streamlit UI Setup

```python
st.title("Language-Translation")
inputtext = st.text_area("Enter your text and listen to how it sounds...", height=100)
choice = st.sidebar.radio('SELECT LANGUAGE', langlist)
```
**Explanation:**
- Displays app title and text input box.
- Sidebar radio buttons allow selecting the output language.

---

## 🔊 5️⃣ Define Speech-Supported Languages

```python
speech_langs = { "en": "English", "fr": "French", "hi": "Hindi", ... }
```
**Explanation:**
- Defines which languages support **speech synthesis** (for gTTS).

---

## 💾 6️⃣ Audio File Download Helper

```python
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href
```
**Explanation:**
- Reads a file, encodes it in Base64, and creates a **download link** in Streamlit.

---

## 🧭 7️⃣ Translation and Audio Output

```python
if len(inputtext) > 0:
    try:
        output = translate(inputtext, lang_array[choice])
        st.text_area("TRANSLATED TEXT", output, height=200)

        if choice in speech_langs.values():
            aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
            aud_file.save("lang.mp3")
            st.audio("lang.mp3")
            st.markdown(get_binary_file_downloader_html("lang.mp3", "⬇️ Download Audio"), unsafe_allow_html=True)
    except Exception as e:
        st.error(e)
```
**Explanation:**
- Checks if text is entered.
- Translates it using the selected language.
- If that language supports speech, it:
  - Converts it to audio (`gTTS`),
  - Plays it in Streamlit,
  - Provides a download button.

---

## ✅ Summary

| Feature | Purpose |
|----------|----------|
| 🎨 Custom CSS | Gives futuristic world-map design |
| 🌐 Translation | Uses `mtranslate` for 60+ languages |
| 🔊 Text-to-Speech | Converts translated text to audio via `gTTS` |
| 💾 Download Option | Base64 link lets users save MP3 |
| 🧱 Streamlit Layout | Two-column responsive interface |

---

**Thanks to open-source contributors and mentors for inspiration! 🙌**  
