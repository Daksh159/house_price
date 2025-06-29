import streamlit as st
import joblib
import numpy as np

# Load model and column order
model = joblib.load("bangalore_linear_model.pkl")
columns = joblib.load("model_columns.pkl")

st.title("🏠 Bangalore House Price Predictor")

# Input fields
total_sqft = st.number_input("Total Square Feet", value=1000)
bhk = st.number_input("Number of Bedrooms (BHK)", step=1, value=2)
bath = st.number_input("Number of Bathrooms", step=1, value=2)
balcony = st.number_input("Number of Balconies", step=1, value=1)
price_per_sqft = st.number_input("Price per Sqft", value=6000)

# Categorical dropdowns (manually or from columns)
location_options = sorted([col.replace("location_", "") for col in columns if col.startswith("location_")])
area_options = [col.replace("area_type_", "") for col in columns if col.startswith("area_type_")]
avail_options = [col.replace("availability_grouped_", "") for col in columns if col.startswith("availability_grouped_")]

location = st.selectbox("Location", location_options)
area_type = st.selectbox("Area Type", area_options)
availability = st.selectbox("Availability", avail_options)

# Prepare input data
input_data = np.zeros(len(columns))

input_data[columns.index('total_sqft')] = total_sqft
input_data[columns.index('bhk')] = bhk
input_data[columns.index('bath')] = bath
input_data[columns.index('balcony')] = balcony
input_data[columns.index('price_per_sqft')] = price_per_sqft

# One-hot encoding
loc_col = f"location_{location}"
area_col = f"area_type_{area_type}"
avail_col = f"availability_grouped_{availability}"

if loc_col in columns:
    input_data[columns.index(loc_col)] = 1
if area_col in columns:
    input_data[columns.index(area_col)] = 1
if avail_col in columns:
    input_data[columns.index(avail_col)] = 1

# Predict
if st.button("Predict Price"):
    price = model.predict([input_data])[0]
    st.success(f"🏷️ Estimated House Price: ₹{price:.2f} Lakhs")
