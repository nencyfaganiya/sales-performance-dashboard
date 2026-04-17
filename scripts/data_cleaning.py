"""
Data Cleaning and Transformation Script
Demonstrates data quality checks and ETL processes
Author: Nency Faganiya
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_raw_data(filename='sales_data_raw.csv'):
    """Load raw sales data"""
    filepath = f'data/raw/{filename}'
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"✓ Loaded {len(df)} records")
    return df

def perform_data_quality_checks(df):
    """Perform comprehensive data quality checks"""
    print("\n" + "="*60)
    print("DATA QUALITY ASSESSMENT")
    print("="*60)
    
    # Missing values
    print("\n1. Missing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_summary = pd.DataFrame({
        'Missing_Count': missing,
        'Percentage': missing_pct
    })
    print(missing_summary[missing_summary['Missing_Count'] > 0])
    
    # Duplicates
    print(f"\n2. Duplicate Records:")
    duplicates = df.duplicated().sum()
    print(f"   Total duplicates: {duplicates}")
    print(f"   Percentage: {(duplicates/len(df)*100):.2f}%")
    
    # Data types
    print(f"\n3. Data Types:")
    print(df.dtypes)
    
    # Outliers in numeric columns
    print(f"\n4. Potential Outliers (values > 3 std dev):")
    numeric_cols = ['net_revenue', 'profit', 'quantity']
    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()
        outliers = df[(df[col] > mean + 3*std) | (df[col] < mean - 3*std)]
        print(f"   {col}: {len(outliers)} potential outliers")
    
    # Negative values check
    print(f"\n5. Data Validation:")
    negative_revenue = df[df['net_revenue'] < 0]
    print(f"   Negative revenue records: {len(negative_revenue)}")
    
    return True

def clean_data(df):
    """Clean and transform the data"""
    print("\n" + "="*60)
    print("DATA CLEANING PROCESS")
    print("="*60)
    
    initial_count = len(df)
    
    # 1. Remove duplicates
    print("\n1. Removing duplicates...")
    df = df.drop_duplicates()
    print(f"   ✓ Removed {initial_count - len(df)} duplicate records")
    
    # 2. Handle missing values
    print("\n2. Handling missing values...")
    # Fill missing sales_rep with 'Unassigned'
    df['sales_rep'].fillna('Unassigned', inplace=True)
    print(f"   ✓ Filled missing sales_rep values")
    
    # 3. Data type conversions
    print("\n3. Converting data types...")
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    print(f"   ✓ Converted transaction_date to datetime")
    
    # 4. Add derived columns
    print("\n4. Creating derived columns...")
    
    # Profit margin
    df['profit_margin'] = (df['profit'] / df['net_revenue'] * 100).round(2)
    
    # Revenue per unit
    df['revenue_per_unit'] = (df['net_revenue'] / df['quantity']).round(2)
    
    # Flag high-value transactions
    df['is_high_value'] = df['net_revenue'] >= df['net_revenue'].quantile(0.75)
    
    # Days in quarter
    df['days_since_start'] = (df['transaction_date'] - df['transaction_date'].min()).dt.days
    
    print(f"   ✓ Added profit_margin column")
    print(f"   ✓ Added revenue_per_unit column")
    print(f"   ✓ Added is_high_value flag")
    print(f"   ✓ Added days_since_start column")
    
    # 5. Standardize text fields
    print("\n5. Standardizing text fields...")
    text_columns = ['customer_segment', 'region', 'product_category', 'sales_channel']
    for col in text_columns:
        df[col] = df[col].str.strip().str.title()
    print(f"   ✓ Standardized text formatting")
    
    return df

def create_aggregated_tables(df):
    """Create aggregated tables for analysis"""
    print("\n" + "="*60)
    print("CREATING AGGREGATED TABLES")
    print("="*60)
    
    # Monthly summary
    print("\n1. Creating monthly summary...")
    monthly = df.groupby(['year', 'month_num', 'month']).agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'transaction_id': 'count',
        'customer_id': 'nunique',
        'quantity': 'sum'
    }).round(2)
    monthly.columns = ['revenue', 'profit', 'transactions', 'unique_customers', 'units_sold']
    monthly = monthly.reset_index()
    monthly['profit_margin'] = (monthly['profit'] / monthly['revenue'] * 100).round(2)
    monthly.to_csv('data/processed/monthly_summary.csv', index=False)
    print(f"   ✓ Saved monthly_summary.csv")
    
    # Product performance
    print("\n2. Creating product performance summary...")
    product = df.groupby(['product_category', 'product_name']).agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'quantity': 'sum',
        'transaction_id': 'count'
    }).round(2)
    product.columns = ['revenue', 'profit', 'units_sold', 'transactions']
    product = product.reset_index()
    product['avg_transaction_value'] = (product['revenue'] / product['transactions']).round(2)
    product = product.sort_values('revenue', ascending=False)
    product.to_csv('data/processed/product_performance.csv', index=False)
    print(f"   ✓ Saved product_performance.csv")
    
    # Regional performance
    print("\n3. Creating regional performance summary...")
    regional = df.groupby(['region', 'city']).agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'transaction_id': 'count',
        'customer_id': 'nunique'
    }).round(2)
    regional.columns = ['revenue', 'profit', 'transactions', 'unique_customers']
    regional = regional.reset_index()
    regional['revenue_per_customer'] = (regional['revenue'] / regional['unique_customers']).round(2)
    regional = regional.sort_values('revenue', ascending=False)
    regional.to_csv('data/processed/regional_performance.csv', index=False)
    print(f"   ✓ Saved regional_performance.csv")
    
    # Customer segment analysis
    print("\n4. Creating customer segment analysis...")
    segment = df.groupby('customer_segment').agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'transaction_id': 'count',
        'customer_id': 'nunique'
    }).round(2)
    segment.columns = ['revenue', 'profit', 'transactions', 'unique_customers']
    segment = segment.reset_index()
    segment['avg_revenue_per_customer'] = (segment['revenue'] / segment['unique_customers']).round(2)
    segment['avg_transaction_value'] = (segment['revenue'] / segment['transactions']).round(2)
    segment.to_csv('data/processed/customer_segment_analysis.csv', index=False)
    print(f"   ✓ Saved customer_segment_analysis.csv")
    
    return True

def save_cleaned_data(df, filename='sales_data_cleaned.csv'):
    """Save cleaned data"""
    filepath = f'data/processed/{filename}'
    df.to_csv(filepath, index=False)
    print(f"\n✓ Cleaned data saved to {filepath}")
    
    # Display summary
    print(f"\nCleaned Data Summary:")
    print(f"Total Records: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    print(f"Date Range: {df['transaction_date'].min()} to {df['transaction_date'].max()}")
    print(f"Total Revenue: £{df['net_revenue'].sum():,.2f}")
    print(f"Total Profit: £{df['profit'].sum():,.2f}")

if __name__ == "__main__":
    # Load raw data
    df = load_raw_data()
    
    # Perform quality checks
    perform_data_quality_checks(df)
    
    # Clean data
    df_clean = clean_data(df)
    
    # Create aggregated tables
    create_aggregated_tables(df_clean)
    
    # Save cleaned data
    save_cleaned_data(df_clean)
    
    print("\n" + "="*60)
    print("Data cleaning complete!")
    print("Next step: Run kpi_calculations.py to calculate business metrics")
    print("="*60)
