import streamlit as st
import numpy as np
import joblib
from google.cloud import firestore
import time
from google.oauth2 import service_account
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(layout="wide")

# Authenticate to Firestore with the JSON account key
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="apneaassist-acf2c")

# Define tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Home", "Screening Quiz", "More Information", "Donate", "About Me + Contact Us", "Q&A"
])

# Helper function to load the model
@st.cache_resource
def load_model():
    return joblib.load('best_random_forest_model.joblib')

# Function to set the language
def set_language(tab_number, languages_key):
    if f"selected_language{tab_number}" in st.session_state:
        lang = st.session_state[f"selected_language{tab_number}"]
        # Update query parameters
        new_query_params = {**st.query_params, f"lang{tab_number}": languages_key[lang]}
        query_string = "&".join([f"{key}={value}" for key, value in new_query_params.items()])
        js_code = f"""
        <script>
        const newUrl = window.location.origin + window.location.pathname + "?{query_string}";
        window.history.replaceState(null, "", newUrl);
        </script>
        """
        components.html(js_code, height=0)
        return lang
    return "English"

# Language options
languages = {"English": "eng", "Spanish": "esp", "Hindi": "hin"}

# Tab 1: Home
with tab1:
    sel_lang1 = st.radio("Language", options=languages.keys(), horizontal=True, key="selected_language1")
    selected_language1 = set_language(1, languages)
    st.markdown(f"### Selected Language: {selected_language1}")

    if selected_language1 == "English":
        st.subheader("What is Obstructive Sleep Apnea?")
        st.write("Obstructive sleep apnea (OSA) is a prevalent sleep disorder characterized by repeated interruptions in breathing during sleep...")
    elif selected_language1 == "Spanish":
        st.subheader("¿Qué es la apnea obstructiva del sueño?")
        st.write("La apnea obstructiva del sueño (AOS) es un trastorno del sueño frecuente caracterizado por interrupciones repetidas en la respiración durante el sueño...")
    elif selected_language1 == "Hindi":
        st.subheader("ऑब्सट्रक्टिव स्लीप एपनिया क्या है?")
        st.write("ऑब्सट्रक्टिव स्लीप एपनिया (OSA) एक सामान्य नींद विकार है जिसमें नींद के दौरान सांस लेने में बार-बार रुकावट होती है...")

# Tab 2: Screening Quiz
with tab2:
    sel_lang2 = st.radio("Language", options=languages.keys(), horizontal=True, key="selected_language2")
    selected_language2 = set_language(2, languages)
    st.markdown(f"### Selected Language: {selected_language2}")

    if selected_language2 == "English":
        st.header("Get your screening results today!")
        st.write("Take the quiz to evaluate your risk for obstructive sleep apnea...")
    elif selected_language2 == "Spanish":
        st.header("¡Obtén tus resultados de evaluación hoy!")
        st.write("Realiza el cuestionario para evaluar tu riesgo de apnea obstructiva del sueño...")
    elif selected_language2 == "Hindi":
        st.header("आज ही अपनी स्क्रीनिंग के परिणाम प्राप्त करें!")
        st.write("ऑब्सट्रक्टिव स्लीप एपनिया के जोखिम का आकलन करने के लिए क्विज़ लें...")

# Tab 3: More Information
with tab3:
    sel_lang3 = st.radio("Language", options=languages.keys(), horizontal=True, key="selected_language3")
    selected_language3 = set_language(3, languages)
    st.markdown(f"### Selected Language: {selected_language3}")

    if selected_language3 == "English":
        st.subheader("Find out more about OSA")
        st.write("Explore additional resources, videos, and articles about obstructive sleep apnea.")
    elif selected_language3 == "Spanish":
        st.subheader("Obtén más información sobre la AOS")
        st.write("Explora recursos adicionales, videos y artículos sobre la apnea obstructiva del sueño.")
    elif selected_language3 == "Hindi":
        st.subheader("ओएसए के बारे में अधिक जानकारी प्राप्त करें")
        st.write("ऑब्सट्रक्टिव स्लीप एपनिया के बारे में अधिक जानने के लिए अतिरिक्त संसाधनों, वीडियो और लेखों का अन्वेषण करें।")

# Tab 4: Donate
with tab4:
    sel_lang4 = st.radio("Language", options=languages.keys(), horizontal=True, key="selected_language4")
    selected_language4 = set_language(4, languages)
    st.markdown(f"### Selected Language: {selected_language4}")

    if selected_language4 == "English":
        st.header("Join the Fight Against OSA by Donating Now!")
        st.write("Your contributions help raise awareness and provide resources for obstructive sleep apnea.")
    elif selected_language4 == "Spanish":
        st.header("¡Únete a la lucha contra la AOS donando ahora!")
        st.write("Tus contribuciones ayudan a crear conciencia y proporcionar recursos para la apnea obstructiva del sueño.")
    elif selected_language4 == "Hindi":
        st.header("अभी दान करके ओएसए के खिलाफ लड़ाई में शामिल हों!")
        st.write("आपका योगदान ऑब्सट्रक्टिव स्लीप एपनिया के बारे में जागरूकता बढ़ाने और संसाधन प्रदान करने में मदद करता है।")

# Tab 5: About Me + Contact Us
with tab5:
    sel_lang5 = st.radio("Language", options=languages.keys(), horizontal=True, key="selected_language5")
    selected_language5 = set_language(5, languages)
    st.markdown(f"### Selected Language: {selected_language5}")

    if selected_language5 == "English":
        st.subheader("About Me")
        st.write("I am dedicated to spreading awareness about obstructive sleep apnea...")
    elif selected_language5 == "Spanish":
        st.subheader("Acerca de mí")
        st.write("Estoy dedicada a crear conciencia sobre la apnea obstructiva del sueño...")
    elif selected_language5 == "Hindi":
        st.subheader("मेरे बारे में")
        st.write("मैं ऑब्सट्रक्टिव स्लीप एपनिया के बारे में जागरूकता फैलाने के लिए समर्पित हूं...")

# Tab 6: Q&A
with tab6:
    sel_lang6 = st.radio("Language", options=languages.keys(), horizontal=True, key="selected_language6")
    selected_language6 = set_language(6, languages)
    st.markdown(f"### Selected Language: {selected_language6}")

    if selected_language6 == "English":
        st.subheader("Have questions? Check here!")
        st.write("Find answers to frequently asked questions about obstructive sleep apnea.")
    elif selected_language6 == "Spanish":
        st.subheader("¿Tienes preguntas? ¡Consulta aquí!")
        st.write("Encuentra respuestas a las preguntas frecuentes sobre la apnea obstructiva del sueño.")
    elif selected_language6 == "Hindi":
        st.subheader("कोई सवाल है? यहाँ देखें!")
        st.write("ऑब्सट्रक्टिव स्लीप एपनिया के बारे में अक्सर पूछे जाने वाले सवालों के जवाब पाएं।")
