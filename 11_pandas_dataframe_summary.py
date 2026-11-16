"""
Practice Task 11: Pandas-Powered Dataframe Summarizer and Cleaner

Problem Statement:
Write a Python program using the Pandas library to load a structured dataset, 
handle missing values, compute statistical aggregations, and generate a 
business summary report.

Exercise Purpose:
This introduces professional Data Analytics tooling. While pure Python 
handles basic logic, Pandas is the industry-standard library for data 
manipulation, dataframe wrangling, and exploratory data analysis (EDA).

Example:
    Input: Sales records dataframe with missing values.
    Output: Cleaned dataframe and aggregated revenue metrics by region.
"""

import pandas as pd

def process_and_summarize_sales(data_dict):
    """Cleans missing data and calculates regional revenue aggregations using Pandas."""
    # Convert dictionary to a Pandas DataFrame
    df = pd.DataFrame(data_dict)
    
    # Data Cleaning: Fill missing 'Sales' with the median value of the column
    median_sales = df['Sales'].median()
    df['Sales'] = df['Sales'].fillna(median_sales)
    
    # Data Cleaning: Drop rows where Region is missing
    df = df.dropna(subset=['Region'])
    
    # Aggregation: Group by Region and calculate total and average sales
    summary = df.groupby('Region')['Sales'].agg(['sum', 'mean', 'count']).reset_index()
    summary.rename(columns={'sum': 'Total_Sales', 'mean': 'Avg_Sales', 'count': 'Transaction_Count'}, inplace=True)
    
    return df, summary


if __name__ == "__main__":
    raw_data = {
        'Region': ['North', 'South', 'North', 'East', 'South', None, 'East'],
        'Product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B', 'Widget C', 'Widget A'],
        'Sales': [250.0, 400.0, None, 150.0, 300.0, 200.0, 350.0]
    }
    
    print("--- Original Raw Data Loaded into DataFrame ---")
    initial_df = pd.DataFrame(raw_data)
    print(initial_df)
    print("\n" + "="*50 + "\n")
    
    cleaned_df, regional_summary = process_and_summarize_sales(raw_data)
    
    print("--- Cleaned DataFrame ---")
    print(cleaned_df)
    print("\n" + "="*50 + "\n")
    
    print("--- Regional Sales Summary KPI Report ---")
    print(regional_summary)