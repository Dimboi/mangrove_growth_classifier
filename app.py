# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('mangrove_growth_model.pkl')

# Judul aplikasi
st.title("Mangrove Growth")

# Sidebar input
st.header("Masukkan Data Mangrove")

tinggi = st.number_input(
    "Berapa tinggi mangrove?(cm) max5000cm",
    min_value=0.0,
    max_value=5000.0,
    step=0.1
)

daun = st.number_input(
    "Berapa kira kira jumlah daun yang terlihat?",
    min_value=0
)

diameter = st.number_input(
    "Berapa cm diameter batang mangrove saat ini? max8cm",
    min_value=0.0,
    max_value=8.0,
    step=0.01
)

akar_udara = st.number_input(
    "Berapa jumlah akar udara yang terlihat? max25",
    min_value=0,
    max_value=25
)

tahun_tanam = st.number_input(
    "Tahun berapakah tanaman ini ditanam?",
    min_value=2000,
    max_value=2030,
    step=1
)

# Tombol prediksi
if st.button("Prediksi Pertumbuhan"):
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
    st.subheader("Hasil Prediksi:")

    if prediction == 'Good Growth':
        st.success("🌿 Pertumbuhan Bagus (Good Growth)")
    elif prediction == 'Normal':
        st.warning("⚠️ Pertumbuhan Normal (Normal)")
    elif prediction == 'Poor Growth':
        st.error("❌ Pertumbuhan Terhambat (Poor Growth)")
    else:
        st.info(f"Pertumbuhan tidak diketahui: {prediction}")
