# 🚀 AI Prediction Suite  
### Full Stack Machine Learning Deployment Platform  

A production-style Full Stack Machine Learning application built using **FastAPI** and **Scikit-Learn**, serving both regression and classification models via REST APIs with a modern web interface.

---

## 📌 Project Overview

AI Prediction Suite demonstrates the complete Machine Learning lifecycle:

- Data loading & preprocessing
- Model training (Regression + Classification)
- Model evaluation
- Model serialization (Joblib)
- REST API deployment using FastAPI
- Real-time inference through interactive frontend
- Production-style project architecture

---

## 🏗 Architecture

Frontend (HTML + CSS + JS)  
⬇  
FastAPI Backend (REST Endpoints)  
⬇  
Scikit-Learn Models (.pkl)  
⬇  
NumPy-based inference pipeline  

---

## 📈 Regression Module

### 🏠 House Price Prediction

- Dataset: California Housing Dataset
- Algorithm: Linear Regression
- Features: 8 numerical input features
- Output: Predicted housing price
- Evaluation Metrics:
  - Mean Squared Error (MSE)
  - R² Score

This module demonstrates supervised regression modeling and real-time prediction serving.

---

## 🩺 Classification Module

### 🔬 Breast Cancer Prediction

- Dataset: Breast Cancer Wisconsin Dataset
- Algorithm: Logistic Regression
- Features: 30 medical measurement inputs
- Output: Malignant or Benign classification
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1 Score

This module demonstrates binary classification deployment via API.

---

## ⚙️ Tech Stack

- FastAPI
- Scikit-Learn
- NumPy
- Joblib
- Jinja2 Templates
- HTML / CSS / JavaScript
- REST Architecture

---

## 📂 Project Structure

```
fullstack-ml-app/
│
├── app.py
├── train_regression.py
├── train_classification.py
├── requirements.txt
│
├── models/
│   ├── regression.pkl
│   └── classifier.pkl
│
└── templates/
    ├── base.html
    ├── home.html
    ├── regression.html
    └── classification.html
```

---

## 🚀 How To Run Locally

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd fullstack-ml-app
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not created yet:

```bash
pip install fastapi uvicorn scikit-learn numpy joblib jinja2 python-multipart
```

---

### 3️⃣ Train Models

```bash
python train_regression.py
python train_classification.py
```

This will generate:

```
models/regression.pkl
models/classifier.pkl
```

---

### 4️⃣ Run FastAPI Server

```bash
uvicorn app:app --port 8001
```

Open in browser:

```
http://127.0.0.1:8001
```

---

## 📊 API Endpoints

### GET /
Home Page

### GET /regression
Regression Prediction UI

### GET /classification
Classification Prediction UI

### POST /predict_regression
Returns predicted house price

### POST /predict_classification
Returns classification result

---

## 🧠 Key Learning Outcomes

- Model training & evaluation
- Model serialization with Joblib
- REST API design using FastAPI
- Template inheritance (Jinja2)
- Real-time inference serving
- Production-ready folder architecture

---
