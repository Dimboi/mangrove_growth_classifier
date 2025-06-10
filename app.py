# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('mangrove_growth_model.pkl')

# Judul aplikasi
st.title("Prediction of the growth of Rhizophora stylosa mangrove type.")

# Sidebar input
st.header("Mangrove Data Input")

tinggi = st.number_input(
    "How tall are the mangroves now? (max 1500 cm)",
    min_value=0.0,
    max_value=1500.0,
    step=0.1
)

daun = st.number_input(
    "How many leaves are visible?",
    min_value=0
)

diameter = st.number_input(
    "What is the current diameter of the mangrove stem? (max 8cm)",
    min_value=0.0,
    max_value=8.0,
    step=0.01
)

akar_udara = st.number_input(
    "How many aerial roots are visible? (max 25)",
    min_value=0,
    max_value=25
)

tahun_tanam = st.number_input(
    "In what year was this mangrove tree planted?",
    min_value=2000,
    max_value=2030,
    step=1
)

# Tombol prediksi
if st.button("growth prediction"):
    # Dataframe input
    input_data = pd.DataFrame({
        'Tinggi (cm)': [tinggi],
        'Jumlah Daun': [daun],
        'Diameter Batang (cm)': [diameter],
        'Jumlah Akar Udara': [akar_udara],
        'Tahun Penanaman': [tahun_tanam]
    })

    # Prediksi
    prediction = model.predict(input_data)[0]

    # Hasil prediksi dengan warna
    st.subheader("Prediction Results:")

    if prediction == 'Good Growth':
        st.success("🌿 Pertumbuhan Bagus (Good Growth)")
    elif prediction == 'Normal':
        st.warning("⚠️ Pertumbuhan Normal (Normal)")
    elif prediction == 'Poor Growth':
        st.error("❌ Pertumbuhan Terhambat (Poor Growth)")
    else:
        st.info(f"Pertumbuhan tidak diketahui: {prediction}")
