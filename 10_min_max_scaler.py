"""
Practice Task 10: Min-Max Feature Scaling / Normalization

Problem Statement:
Write a Python program that takes a list of numeric features and normalizes 
them into a standard range between 0 and 1 using the Min-Max scaling formula:
    X_scaled = (X - X_min) / (X_max - X_min)

Exercise Purpose:
Feature scaling is a core preprocessing step in Machine Learning and Data Analytics. 
Before feeding numeric columns into predictive models, normalizing data prevents 
features with larger numerical ranges from overpowering smaller ones.

Example:
    Input:  [10, 20, 30, 40, 50]
    Output: [0.0, 0.25, 0.5, 0.75, 1.0]
"""

def min_max_scale(data_list):
    """Normalizes a list of numeric values between 0.0 and 1.0."""
    if not data_list or len(data_list) == 0:
        return []
        
    min_val = min(data_list)
    max_val = max(data_list)
    
    # Handle edge case where all values in the dataset are identical
    if min_val == max_val:
        return [0.0 for _ in data_list]
        
    scaled_data = [(x - min_val) / (max_val - min_val) for x in data_list]
    return [round(val, 4) for val in scaled_data]


if __name__ == "__main__":
    raw_features = [15, 30, 45, 60, 100]
    print(f"Raw Input Features: {raw_features}")
    
    normalized_features = min_max_scale(raw_features)
    print(f"Normalized (Min-Max Scaled): {normalized_features}")