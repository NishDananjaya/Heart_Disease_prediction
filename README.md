# Heart Disease Prediction using Machine Learning

This repository contains a web application for predicting heart disease using various machine learning algorithms. The application is built with Streamlit and allows users to input various health metrics to predict the likelihood of heart disease.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms Used](#algorithms-used)
- [Model Training](#model-training)
- [Disclaimer](#disclaimer)
- [License](#license)

## Overview

The application leverages machine learning models to predict heart disease based on user input. It includes a user-friendly interface for inputting health metrics such as age, gender, chest pain type, and more. The application uses a pre-trained model to provide predictions.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
    ```sh
    https://github.com/NishDananjaya/Heart_Disease_prediction.git
    ```

2. Change directory into the project folder:
    ```sh
    cd heart-disease-prediction
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

After running the application, open your web browser and navigate to `http://localhost:8501`. You will see a form where you can input the following information:

- Age
- Gender
- Chest pain types
- Resting blood pressure
- Serum Cholesterol in mg/dl
- Fasting Blood Sugar > 120 mg/dl
- Resting Electrocardiographic Results
- Maximum heart rate achieved
- Exercise induced angina
- ST depression induced by exercise relative to rest
- Slope of the peak exercise ST segment
- Number of major vessels colored by fluoroscopy
- Thalassemia

Click the 'Heart Disease Test Result' button to get the prediction.

## Algorithms Used

The following machine learning algorithms were used to train the model:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- XGBoost
- Decision Tree
- Naive Bayes
- Neural Network

## Model Training

The model was trained using the following process:

1. Data Preprocessing:
    - Data normalization using `StandardScaler`.

2. Model Training:
    - Multiple algorithms were trained and evaluated.
    - The best-performing model was selected and saved.

3. Model Saving:
    - The final model and scaler were saved using `pickle` for later use in the Streamlit application.

## Disclaimer

**Disclaimer:** This application is for educational purposes only. Always consult a medical professional for medical advice.

