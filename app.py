from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load models
reg_model = joblib.load("models/regression.pkl")
clf_model = joblib.load("models/classifier.pkl")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/regression", response_class=HTMLResponse)
def regression_page(request: Request):
    return templates.TemplateResponse("regression.html", {"request": request})


@app.get("/classification", response_class=HTMLResponse)
def classification_page(request: Request):
    return templates.TemplateResponse("classification.html", {"request": request})


@app.post("/predict_regression")
def predict_regression(features: str = Form(...)):
    values = np.array([float(i) for i in features.split(",")]).reshape(1, -1)
    prediction = reg_model.predict(values)
    return {"prediction": float(prediction[0])}


@app.post("/predict_classification")
def predict_classification(features: str = Form(...)):
    values = np.array([float(i) for i in features.split(",")]).reshape(1, -1)
    prediction = clf_model.predict(values)
    return {"prediction": int(prediction[0])}