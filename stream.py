import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
import pandas as pd

# Setting Webpage Configurations
st.set_page_config(page_icon="🎶",page_title="Audio Extracter", layout="wide")

st.markdown("<h1 style='text-align: center; color: blue;'>🎶 Audio Subtitle Extracter 🎧</h1>",unsafe_allow_html=True)

#st.title(':blue[Audio Subtitle Extracter 🎧]')

tab1, tab2 = st.tabs(["Main Tab", "Extraction Tab"])

with tab1:
    col1, col2 = st.columns(2,gap='large')

    with col1:
        st.write('### :red[Project]')
        st.write("Extracting Audio Subtitles from Tamil Videos")

        st.write('### :red[Problem Statement]')
        st.write('The primary objective of this project is to develop a curated and legally obtained dataset of Audios of Tamil or Hindi videos and its subtitles in the respective language (SRT files) specifically focusing on Tamil or Hindi movies or any videos in the same language based on your choice')
         
    with col2:
        st.write("### :red[Tools and Technologies Used]")
        st.write("* Python")
        st.write('* Streamlit')
        st.write('* Speech Recognition')
        st.write('* Selenium')
        st.write('* Deep Translator')
        st.write("* Pandas")
        st.write("* Google Translate")
        st.write("* pydub")
        st.write("* Requests")


        
with tab2:    

    audio_file_uploader = st.file_uploader("Upload a .WAV file")
    submit = st.button('Extract')

    # initialize the recognizer
    recognizer = sr.Recognizer()

    # Create a Translator object
    translator = GoogleTranslator(source='ta', target='en')

    # Audio file --> Audio Data --> Text

    data = []

    try:
        with st.spinner('Extracting...'):
            if audio_file_uploader and submit:
                audio_file = sr.AudioFile(audio_file_uploader)

                with audio_file as source:
                    audio_data = recognizer.record(source)
                    
                text = recognizer.recognize_google(audio_data, language = 'ta-IN')

                translated_text = translator.translate(text)

                data_dict = {'filename':audio_file_uploader.name,
                            'Tamil_subtitle': text,
                            'English_subtitle':translated_text}

                data.append(data_dict)

                new_df = pd.DataFrame(data = data)
                st.dataframe(new_df, width = 1200, hide_index = True)
                st.success('Info Extraxted Successfully')

    except:
        st.warning('Please check your internet connection')
