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
    "Berapa tinggi mangrove? (cm)",
    min_value=0.0,
    step=0.1
)

daun = st.number_input(
    "Berapa kira kira jumlah daun yang terlihat?",
    min_value=0
)

diameter = st.number_input(
    "Berapa cm diameter batang mangrove saat ini?",
    min_value=0.0,
    step=0.01
)

akar_udara = st.number_input(
    "Berapa jumlah akar udara yang terlihat?",
    min_value=0
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

    # Hasil prediksi
    st.subheader("Hasil Prediksi:")
    st.success(f"Mangrove ini diprediksi mengalami pertumbuhan: **{prediction}**")
