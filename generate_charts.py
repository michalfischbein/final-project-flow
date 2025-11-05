#!/usr/bin/env python
# generate_charts.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully from", file_path)
        return df
    except Exception as e:
        print("Error loading data:", e)
        raise

def create_scatter_plot(df):
    try:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='Discount', y='Profit')
        plt.title('Relationship between Discount Percentage and Profit Margins')
        plt.xlabel('Discount Percentage')
        plt.ylabel('Profit Margin')
        plt.savefig('chart_1.png')
        plt.show()
        print("Scatter plot saved as chart_1.png")
    except Exception as e:
        print("Failed to generate scatter plot:", e)

def create_line_chart(df):
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        sales_time = df.resample('M', on='Order Date').sum()
        plt.figure(figsize=(12, 6))
        plt.plot(sales_time.index, sales_time['Sales'])
        plt.title('Sales Volume Over Time with Peak Period Annotations')
        plt.xlabel('Order Date')
        plt.ylabel('Sales Volume')
        plt.savefig('chart_2.png')
        plt.show()
        print("Line chart saved as chart_2.png")
    except Exception as e:
        print("Failed to generate line chart:", e)

def create_bar_chart(df):
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['is_outlier'] = (np.abs(df['Sales'] - df['Sales'].mean()) > 3 * df['Sales'].std())
        sales_time = df.resample('M', on='Order Date').sum()
        plt.figure(figsize=(12, 6))
        plt.bar(sales_time.index, sales_time['Sales'], 
                color=['red' if is_out else 'blue' for is_out in sales_time['is_outlier']])
        plt.title('Sales Volume with Outliers Highlighted')
        plt.xlabel('Order Date')
        plt.ylabel('Sales Volume')
        plt.savefig('chart_3.png')
        plt.show()
        print("Bar chart saved as chart_3.png")
    except Exception as e:
        print("Failed to generate bar chart:", e)

def main():
    file_path = 'data_cleaned.csv'
    df = load_data(file_path)
    create_scatter_plot(df)
    create_line_chart(df)
    create_bar_chart(df)

if __name__ == "__main__":
    main()

# This script will generate the following charts:
# - Scatter plot of Discount vs Profit (chart_1.png)
# - Line chart showing Sales Volume Over Time (chart_2.png)
# - Bar chart of Sales Volume with Outliers Highlighted (chart_3.png)
#```
#This script combines the visualization code into one executable Python script that loads data, generates the specified charts, and saves them as image files with progress tracking and error handling.