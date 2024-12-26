# Wine Quality Prediction

This project implements a Wine Quality Prediction Web Application as part of an end-to-end MLOps pipeline. The application predicts wine quality based on its physicochemical properties using a machine learning model. It leverages Flask for creating a user-friendly interface and MLflow for model tracking and versioning. The project is deployed on Heroku with automated CI/CD pipelines to ensure seamless deployment and continuous integration.



---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Running the Application](#running-the-application)
6. [Project Workflow](#project-workflow)
7. [Usage](#usage)
8. [Future Improvements](#future-improvements)

---

## Project Overview

This project uses physicochemical properties of wine to predict its quality. The machine learning model is trained on historical data, integrated into an MLOps pipeline, and deployed for real-time predictions. The project combines Flask for creating a web-based interface and MLflow for model management and deployment. This solution is valuable for wineries, distributors, and enthusiasts to evaluate wine quality effectively and efficiently.

### Input Features:
- **Fixed Acidity**: Expected range 4.6 to 15.9
- **Volatile Acidity**: Expected range 0.12 to 1.58
- **Citric Acid**: Expected range 0.0 to 1
- **Residual Sugar**: Expected range 0.9 to 15.5
- **Chlorides**: Expected range 0.012 to 0.611
- **Free Sulfur Dioxide**: Expected range 1 to 72
- **Total Sulfur Dioxide**: Expected range 6 to 289
- **Density**: Expected range 0.990 to 1.003
- **pH**: Expected range 2.74 to 4.01
- **Sulphates**: Expected range 0.33 to 2
- **Alcohol**: Expected range 8.4 to 14.9

### Output:
- Predicted Wine Quality (Scale: 3 to 8)

---

## Features

- End-to-end MLOps pipeline for model development, testing, and deployment.
- Integration with MLflow for model tracking and versioning.
- Flask-based web application for real-time predictions.
- Modular and scalable code structure.
- Hyperparameter tuning using GridSearchCV for optimal model performance.

---

## Technologies Used

- **Programming Language**: Python (3.9)
- **Libraries**:
  - Flask
  - Scikit-learn
  - MLflow
  - Pandas
  - NumPy
  - Joblib
  - Logging
- **Tools**: SQLite (for database management), VS Code

---

## Setup Instructions

Follow the steps below to set up the project on macOS.

### Prerequisites
Ensure you have the following installed:
- Python (>=3.9)
- pip (Python package manager)
- Virtual environment support (`venv` or `virtualenv`)

### Step 1: Clone the Repository
```bash
# Clone the repository
git clone https://github.com/ssantrupth/simple-dvc-demo.git
cd simple-dvc-demo
```

### Step 2: Create a Virtual Environment
```bash
# Create a virtual environment
python3 -m venv wineq

# Activate the virtual environment
source wineq/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Installation
Ensure all required packages are installed successfully.
```bash
pip list
```

---

## Running the Application

1. Activate the virtual environment (if not already activated):
    ```bash
    source project/bin/activate
    ```

2. Start the Flask server:
    ```bash
    python app.py
    ```

3. Open your browser and navigate to:
    ```
    http://127.0.0.1:4000
    ```

---

## Project Workflow

1. **Data Ingestion**:
   - Data is collected from CSV files and preprocessed.

2. **Model Training**:
   - Multiple regression models are trained and evaluated.
   - Hyperparameter tuning is performed using GridSearchCV.

3. **Model Evaluation**:
   - The best model is selected based on R2 score.

4. **Model Deployment**:
   - The best-performing model is saved and integrated into the Flask application for real-time predictions.
   - MLflow is used for tracking and managing model versions.

5. **Web Application**:
   - Users input wine attributes to get predicted wine quality.

---

## Usage

1. Open the Flask app in your browser.
2. Fill in the form with the following details:
   - Fixed Acidity
   - Volatile Acidity
   - Citric Acid
   - Residual Sugar
   - Chlorides
   - Free Sulfur Dioxide
   - Total Sulfur Dioxide
   - Density
   - pH
   - Sulphates
   - Alcohol
3. Submit the form to get the predicted wine quality.

---

## Future Improvements

- Enhance the UI/UX of the web application.
- Extend the MLOps pipeline for CI/CD integration.
- Train the model with additional features for improved accuracy.
- Deploy the application on cloud platforms (e.g., AWS, GCP, or Azure).
- Add database support for storing user inputs and predictions.

---

## Acknowledgments
This project is inspired by real-world wine datasets and aims to assist the wine industry in assessing wine quality efficiently.
