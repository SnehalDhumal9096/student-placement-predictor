# Student Placement Prediction Using Machine Learning

## 1. Project Overview

Student Placement Prediction is a Machine Learning project that predicts whether a student is likely to get placed based on academic, skill-related, and other student attributes.

The project uses a Random Forest Classification model and provides an interactive Streamlit web application for making predictions and viewing Machine Learning insights.

---

## 2. Problem Statement

Placement decisions depend on multiple factors such as academic performance, skills, internships, projects, aptitude performance, and other student characteristics.

The objective of this project is to develop a Machine Learning model that can learn patterns from historical student placement data and predict the placement outcome of a student.

---

## 3. Objectives

- Analyze student placement data.
- Perform data preprocessing and exploratory data analysis.
- Identify important features related to placement.
- Train multiple Machine Learning classification models.
- Compare model performance.
- Select the best-performing model.
- Use Random Forest for final placement prediction.
- Analyze feature importance.
- Build an interactive Streamlit application.
- Provide ML-based insights through the application.

---

## 4. Dataset

### Dataset Name

Indian Student Placement Dataset 2025

### Dataset File

Indian_Student_Placement_Dataset_2025.csv

The dataset contains information about students and their placement outcomes.

The features are used to train a supervised Machine Learning classification model.

The target variable represents the student's placement outcome.

---

## 5. Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

### Machine Learning

- Classification
- Random Forest
- Model Evaluation
- Feature Importance

### Application

- Streamlit

### Development Environment

- Google Colab
- Python

### Version Control

- Git
- GitHub

---

## 6. Project Workflow

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

---

## 7. Data Preprocessing

Data preprocessing was performed before training the Machine Learning models.

A Scikit-learn preprocessing pipeline was used to apply the required transformations to the dataset.

The same preprocessing pipeline is saved and reused by the Streamlit application.

---

## 8. Machine Learning Model

Different classification algorithms were evaluated during the project.

The final model selected for the application is the Random Forest Classifier.

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to make predictions.

Advantages of Random Forest include:

- Handles nonlinear relationships.
- Provides good classification performance.
- Reduces overfitting compared with a single decision tree.
- Can calculate feature importance.
- Works well with many types of datasets.

---

## 9. Final Model

The final placement prediction model is a Random Forest Classifier.

The trained model is saved as:

models/random_forest_model.pkl

The preprocessing pipeline is saved as:

models/preprocessor.pkl

These files allow the trained model to be reused without retraining it every time the application starts.

---

## 10. Feature Importance Analysis

Feature importance was calculated using the Random Forest model.

Feature importance helps identify which features were most useful to the model when making placement predictions.

The top features are displayed in the Streamlit application under the ML Insights section.

The feature importance chart is stored as:

images/feature_importance.png

The complete feature importance data is stored as:

feature_importance.csv

Feature importance indicates how useful a feature was to the trained model. It does not necessarily mean that the feature directly causes a student to get placed.

---

## 11. Streamlit Application

A Streamlit web application was developed to provide an interactive interface for the project.

The application contains:

### Placement Prediction

Allows users to enter student information and obtain a placement prediction.

### ML Insights

Displays:

- Top important features
- Feature importance values
- Feature importance chart
- Top placement-influencing features
- Explanation of feature importance

---

## 12. Model Evaluation

The Machine Learning models were evaluated using classification metrics.

Important evaluation metrics include:

### Accuracy

Accuracy measures the percentage of predictions that were correct.

### Precision

Precision measures how many of the students predicted as placed were actually placed.

### Recall

Recall measures how many of the actually placed students were correctly identified by the model.

### F1 Score

F1 Score provides a balance between precision and recall.

### Confusion Matrix

The confusion matrix shows True Positives, True Negatives, False Positives, and False Negatives.

---

## 13. Advantages

- Uses Machine Learning for placement prediction.
- Provides an interactive user interface.
- Uses a trained Random Forest model.
- Provides feature importance insights.
- Model and preprocessing pipeline are saved for reuse.
- Demonstrates an end-to-end Machine Learning project.

---

## 14. Limitations

- Predictions depend on the quality of the dataset.
- The model cannot guarantee actual placement.
- Feature importance does not establish causation.
- Real-world recruitment decisions depend on many factors.
- Model performance may change on different datasets.

---

## 15. Future Scope

- Add more student and recruitment-related features.
- Train the model on a larger dataset.
- Add probability-based prediction.
- Add personalized recommendations.
- Add explainable AI techniques such as SHAP.
- Deploy the Streamlit application online.
- Add a database for storing predictions.
- Continuously retrain the model using new placement data.

---

## 16. Conclusion

This project demonstrates how Machine Learning can be applied to student placement prediction.

The project follows an end-to-end Machine Learning workflow including data preprocessing, exploratory data analysis, model training, model comparison, Random Forest model selection, feature importance analysis, and Streamlit deployment.

The final application provides both placement prediction functionality and ML-based insights about the factors used by the model.