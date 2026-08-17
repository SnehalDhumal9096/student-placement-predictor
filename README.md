# Student Placement Prediction Using Machine Learning

## 📌 Project Overview

Student Placement Prediction is a Machine Learning project that predicts whether a student is likely to get placed based on academic, skill-related, and other student attributes.

The project uses a Random Forest Classification model and provides an interactive Streamlit web application for making predictions and viewing Machine Learning insights.

## 🎯 Objectives

- Analyze student placement data
- Perform data preprocessing and exploratory data analysis
- Identify important features related to placement
- Train and compare Machine Learning classification models
- Select the best-performing model
- Use Random Forest for final placement prediction
- Analyze feature importance
- Build an interactive Streamlit application
- Provide ML-based insights through the application

## 📊 Dataset

**Dataset:** Indian Student Placement Dataset 2025

**File:** `Indian_Student_Placement_Dataset_2025.csv`

The dataset contains information about students and their placement outcomes.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Google Colab
- Git
- GitHub

## 🔄 Project Workflow

1. Dataset Collection
2. Data Loading
3. Data Understanding
4. Data Cleaning
5. Data Preprocessing
6. Exploratory Data Analysis
7. Train-Test Split
8. Model Training
9. Model Comparison
10. Best Model Selection
11. Feature Importance Analysis
12. Streamlit Application
13. Model Saving
14. Documentation

## 🤖 Machine Learning Model

The final model selected for the application is the **Random Forest Classifier**.

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to make predictions.

The trained model and preprocessing pipeline are saved as `.pkl` files so that the application can use them without retraining the model.

## 📈 Feature Importance

Feature importance is calculated using the Random Forest model.

It helps identify which features were most useful to the model when making placement predictions.

The project includes:

- `feature_importance.csv`
- `images/feature_importance.png`

## 🌐 Streamlit Application

The project includes an interactive Streamlit web application.

The application provides:

### Placement Prediction
Users can enter student information and obtain a placement prediction.

### ML Insights
The application displays important features and feature-importance information used by the model.

## 📁 Project Structure

```text
student-placement-prediction/
│
├── app.py
├── requirements.txt
├── .gitignore
├── feature_importance.csv
│
├── data/
│   └── Indian_Student_Placement_Dataset_2025.csv
│
├── models/
│   ├── placement_model.pkl
│   └── placement_preprocessor.pkl
│
├── notebooks/
│   └── MLProject_week1.ipynb
│
├── images/
│   └── feature_importance.png
│
└── docs/
    └── project_documentation.md