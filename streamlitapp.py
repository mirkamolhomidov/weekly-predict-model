import streamlit as st
import pandas as pd
import joblib

model = joblib.load("store_model.pkl")
st.title("Haftalik Savdo Bashorati")

store = st.number_input("Do'kon raqami", min_value=1, max_value=45, step=1)
temperature = st.number_input("Harorat")
fuel_price = st.number_input("Yoqilg'i narxi")
cpi = st.number_input("Iste'mol narxlari indeksi")
unemployment = st.number_input("Ishsizlik darajasi")
holiday = st.selectbox("Bayram haftasimi?", ['Yo‘q', 'Ha'])
year = st.selectbox("Yil", [2010, 2011, 2012])
month = st.selectbox("Oy", list(range(1, 13)))
day = st.selectbox("Kun", list(range(1, 32)))

if st.button("Wamart do'koni savdosini predict qilish"):
    input_data = pd.DataFrame([{
        "Store": store,
        "Holiday_Flag": 1 if holiday == 'Ha' else 0,
        "Temperature": temperature,
        "Fuel_Price": fuel_price,
        "CPI": cpi,
        "Unemployment": unemployment,
        "Year": year,
        "Month": month,
        "Day": day
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Predict qilingan haftalik savdo: ${int(prediction):,}")
