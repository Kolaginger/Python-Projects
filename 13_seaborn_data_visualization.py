"""
Practice Task 13: Exploratory Data Visualization with Seaborn

Problem Statement:
Write a Python program using Seaborn and Matplotlib to load a dataset 
and generate an exploratory data visualization (such as a scatter plot 
with categorical groupings).

Exercise Purpose:
Data visualization is a core component of Exploratory Data Analysis (EDA). 
For Data Analytics and AI programs, being able to visually communicate trends, 
correlations, and anomalies is just as important as building the models.

Example:
    Input: Numerical dataframe of features (e.g., advertising spend vs sales).
    Output: Generates a styled Seaborn exploratory plot.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def generate_sales_visualization(df):
    """Generates a styled Seaborn scatter plot mapping variables and regions."""
    # Set professional visual theme using seaborn
    sns.set_theme(style="whitegrid")
    
    # Create figure canvas
    plt.figure(figsize=(8, 5))
    
    # Generate scatter plot with categorical hue mapping
    sns.scatterplot(
        data=df, 
        x='Advertising_Spend', 
        y='Revenue', 
        hue='Region', 
        palette='deep', 
        s=120
    )
    
    plt.title("Advertising Spend vs. Revenue by Region", fontsize=14, fontweight='bold')
    plt.xlabel("Advertising Spend ($)", fontsize=12)
    plt.ylabel("Revenue ($)", fontsize=12)
    
    # Optimize layout for clean presentation
    plt.tight_layout()


if __name__ == "__main__":
    data = {
        'Advertising_Spend': [100, 200, 300, 400, 500, 600, 700, 800],
        'Revenue': [120, 220, 350, 410, 530, 600, 720, 850],
        'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'North', 'South']
    }
    
    df_sample = pd.DataFrame(data)
    
    print("--- Executing Exploratory Data Visualization Pipeline ---")
    generate_sales_visualization(df_sample)
    print("Visualization generated successfully!")
    print("Tip: Run plt.show() if executing in a local GUI environment to render the plot.")