import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Nepal House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Nepal RCC House Price Prediction")
st.write("Predict the estimated cost of an RCC house based on location and construction details.")

# -------------------------------
# LOAD MODEL (SAFE PATH)
# -------------------------------
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "nepal_house_price_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("❌ Model file could not be loaded.")
    st.stop()

# -------------------------------
# USER INPUTS
# -------------------------------
location = st.selectbox(
    "City",
    ["Kathmandu", "Pokhara", "Chitwan", "Dhangadi", "Syangja"]
)

land_area = st.number_input(
    "Land Area (sqft)",
    min_value=500,
    max_value=5000,
    step=50
)

floors = st.slider("Number of Floors", 1, 4)
bedrooms = st.slider("Bedrooms", 1, 6)
bathrooms = st.slider("Bathrooms", 1, 4)
windows = st.slider("Windows", 2, 20)
doors = st.slider("Doors", 2, 10)

cement_bags = st.number_input(
    "Cement Bags Used",
    min_value=100,
    max_value=600,
    step=10
)

plumbing = st.checkbox("Plumbing Installed")
electricity = st.checkbox("Electricity Installed")

# -------------------------------
# PREPARE INPUT DATAFRAME
# -------------------------------
input_df = pd.DataFrame([{
    "location": location,
    "land_area_sqft": land_area,
    "floors": floors,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "windows": windows,
    "doors": doors,
    "cement_bags": cement_bags,
    "rcc_structure": 1,
    "plumbing": int(plumbing),
    "electricity": int(electricity),
    "land_cost": 0,
    "construction_cost": 0,
    "material_cost": 0
}])

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("💰 Predict House Price"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🏷️ Estimated House Price: NPR {prediction:,.0f}")
    except Exception as e:
        st.error("Prediction failed. Please check input values.")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("📊 Model trained on synthetic Nepal RCC housing data (1000 records)")
