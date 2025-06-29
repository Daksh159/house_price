🏠 Bangalore House Price Predictor

A web app built with **Streamlit** and **Scikit-Learn** that predicts house prices in Bangalore based on user inputs like location, square footage, number of bedrooms, and more.

[![Deploy on Render](https://img.shields.io/badge/Live%20Demo-Render-green?style=for-the-badge)](https://bangalore-house-price-m2jn.onrender.com/)

### ✨ Features

* 📊 Predict Bangalore house prices instantly
* 🔢 Inputs include total sqft, BHK, bath, balconies, location, area type, etc.
* 🧠 Uses a pre-trained **Linear Regression** model
* 📁 Clean and minimal UI using **Streamlit**
* 🔒 Safe and local file-based model loading

---

### 🖥️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend/Model**: Scikit-Learn Linear Regression
* **Language**: Python
* **Deployment**: Render

---

### 🚀 How to Run Locally

#### 1. Clone the Repo

```bash
git clone https://github.com/Daksh159/house_price.git
cd house_price
```

#### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the App

```bash
streamlit run app.py
```

---

### 📂 Project Structure

```
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── bangalore_linear_model.pkl  # Trained model
├── model_columns.pkl       # Column transformer data
└── README.md               # This file
