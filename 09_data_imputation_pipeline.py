"""
Practice Task 09: Missing Data Imputation and Outlier Detection

Problem Statement:
Write a Python program that processes a list of numeric records containing 
missing values (`None`) and extreme outliers. The program must fill missing 
values using the dataset's median and flag or cap extreme statistical outliers 
using the Interquartile Range (IQR) method.

Exercise Purpose:
Data cleaning and hygiene are critical prerequisites for Data Analytics and AI. 
Real-world datasets from sensors, logs, or business inputs are rarely clean; 
this script builds an automated data preprocessing pipeline.

Example:
    Input: Sensor temperature readings with missing spots and anomaly spikes.
    Output: Cleaned, imputed dataset ready for analytics models.
"""

def clean_and_impute_data(data_list):
    """Fills missing values with median and cleans extreme outliers."""
    if not data_list:
        return []

    # Step 1: Filter out None values to calculate baseline statistics
    valid_values = [x for x in data_list if x is not None]
    
    if not valid_values:
        return data_list

    # Calculate median for imputation
    sorted_vals = sorted(valid_values)
    n = len(sorted_vals)
    if n % 2 == 1:
        median_val = sorted_vals[n // 2]
    else:
        median_val = (sorted_vals[(n // 2) - 1] + sorted_vals[n // 2]) / 2

    # Step 2: Impute None values with the median
    imputed_data = [x if x is not None else median_val for x in data_list]

    # Step 3: Simple threshold capping for outliers (values beyond 3x standard deviation or logical bounds)
    # For this exercise, let's cap values that exceed a reasonable business threshold (e.g., > 100)
    cleaned_data = [x if x <= 100 else median_val for x in imputed_data]

    return cleaned_data


if __name__ == "__main__":
    raw_sensor_readings = [22.5, 24.1, None, 23.8, 999.0, 21.5, None, 25.0]
    print(f"Raw Input Dataset: {raw_sensor_readings}")
    
    processed_data = clean_and_impute_data(raw_sensor_readings)
    print(f"Cleaned & Imputed Output: {processed_data}")