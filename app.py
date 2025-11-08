import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64


# Custom CSS styling
st.markdown("""
<style>
/* ---- Background Image ---- */
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.4),
        rgba(0, 0, 0, 0.4)
    ),
    url("https://static.vecteezy.com/system/resources/previews/025/751/360/non_2x/futuristic-glowing-world-map-network-connection-3d-blue-earth-map-background-with-plexus-lines-digital-network-for-business-concept-big-data-stream-technology-world-data-analytics-background-vector.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* ---- Text input and text area ---- */
div[data-baseweb="textarea"], div[data-baseweb="input"] {
    background-color: rgba(255, 255, 255, 0.85); /* box color */
    color: #000000;  /* text color inside box */
    border-radius: 10px;
    padding: 8px;
}

/* ---- Sidebar & Radio Buttons ---- */
section[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
}

/* ---- Buttons ---- */
button[kind="primary"] {
    background-color: #008CBA;
    color: white;
    border-radius: 8px;
    border: none;
}
button[kind="primary"]:hover {
    background-color: #005f73;
    color: white;
}
</style>
""", unsafe_allow_html=True)



df = pd.read_csv(r'C:\Users\VICTUS\Desktop\mastering git\Practise git\Global-_Voice-_Translator\language.csv')
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist = tuple(lang)
langcode = df['iso'].to_list()

lang_array ={lang[i]: langcode[i] for i in range(len(langcode))}

st.title("Language-Translation")
inputtext = st.text_area("Enter your text and listen to how it sounds in different languages 🎧🌍",height=100)

choice = st.sidebar.radio('SELECT LANGUAGE',langlist)

speech_langs = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "od" : "odia",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese"    
}

def get_binary_file_downloader_html(bin_file,file_label='File'):
    with open(bin_file,'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}"download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

c1 ,c2 = st.columns([4,3])

if len(inputtext) > 0:
    try :
        output = translate(inputtext,lang_array[choice])
        with c1:
            st.text_area("TRANSLATED TEXT",output,height=200)
            
            if choice in speech_langs.values():
                with c2:
                    aud_file = gTTS(text=output,lang=lang_array[choice],slow=False)
                    aud_file.save("lang.mp3")               
                    audio_file_read = open('lang.mp3', 'rb') 
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.audio(audio_bytes, format='audio/mp3')
                    st.markdown(
    f"""
    <div style="text-align:center; margin-top:10px;">
      {get_binary_file_downloader_html("lang.mp3", "⬇️ Download Audio")}
    </div>
    """,
    unsafe_allow_html=True
)


    except Exception as e:
        st.error(e)
