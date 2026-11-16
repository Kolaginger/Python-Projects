"""
Practice Task 12: Applied Machine Learning with Scikit-Learn

Problem Statement:
Write a Python program using Scikit-Learn to train a simple Linear 
Regression model on numerical features and generate predictive outputs.

Exercise Purpose:
This introduces Applied Machine Learning. For AI and Data Analytics programs demonstrating the ability to instantiate, 
train, and evaluate models using Scikit-Learn proves you are ready for advanced coursework.

Example:
    Input: Feature matrix (e.g., house square footage) and target labels (prices).
    Output: Trained model coefficients, intercept, and target predictions.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

def train_linear_model(X, y):
    """Trains a Linear Regression model and returns coefficients and predictions."""
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    return model, predictions


if __name__ == "__main__":
    # Sample data: House size in square feet (feature) vs Price in thousands (target)
    X = np.array([[650], [800], [1200], [1500], [2000]])
    y = np.array([150, 180, 260, 310, 400])
    
    print("--- Training Scikit-Learn Linear Regression Model ---")
    trained_model, preds = train_linear_model(X, y)
    
    print(f"Model Coefficient (Slope): {trained_model.coef_[0]:.2f}")
    print(f"Model Intercept: {trained_model.intercept_:.2f}")
    print(f"Predictions: {np.round(preds, 2)}")