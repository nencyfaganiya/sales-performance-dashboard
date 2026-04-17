"""
Sales Data Generation Script
Generates realistic synthetic sales data for BI analysis
Author: Nency Faganiya
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_sales_data(num_records=5000, start_date='2022-01-01', end_date='2024-12-31'):
    """
    Generate synthetic sales data with realistic business patterns
    
    Parameters:
    - num_records: Number of sales transactions to generate
    - start_date: Start date for sales data
    - end_date: End date for sales data
    
    Returns:
    - DataFrame with sales transactions
    """
    
    print(f"Generating {num_records} sales records...")
    
    # Date range
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    date_range = (end - start).days
    
    # Product categories and names
    products = {
        'Electronics': ['Laptop Pro', 'Wireless Mouse', 'USB-C Hub', 'Bluetooth Headphones', 'Webcam HD'],
        'Furniture': ['Office Chair', 'Standing Desk', 'Bookshelf', 'Filing Cabinet', 'Desk Lamp'],
        'Stationery': ['Notebook Set', 'Pen Collection', 'Sticky Notes', 'Paper Ream', 'Stapler'],
        'Software': ['Productivity Suite', 'Design Pro', 'Security Pack', 'Cloud Storage', 'Project Manager']
    }
    
    # Regions and cities
    regions = {
        'North': ['Manchester', 'Leeds', 'Liverpool', 'Newcastle'],
        'South': ['London', 'Brighton', 'Southampton', 'Bristol'],
        'East': ['Norwich', 'Cambridge', 'Ipswich', 'Colchester'],
        'West': ['Birmingham', 'Cardiff', 'Plymouth', 'Exeter']
    }
    
    # Customer segments
    customer_segments = ['Enterprise', 'SMB', 'Individual', 'Government']
    
    # Sales channels
    sales_channels = ['Online', 'Direct Sales', 'Partner', 'Retail']
    
    # Generate data
    data = []
    
    for i in range(num_records):
        # Date with seasonal patterns (more sales in Q4)
        random_days = random.randint(0, date_range)
        transaction_date = start + timedelta(days=random_days)
        month = transaction_date.month
        
        # Seasonal multiplier (higher in Q4)
        seasonal_factor = 1.3 if month in [10, 11, 12] else 1.0
        
        # Select product
        category = random.choice(list(products.keys()))
        product = random.choice(products[category])
        
        # Select region and city
        region = random.choice(list(regions.keys()))
        city = random.choice(regions[region])
        
        # Customer details
        customer_id = f"CUST{random.randint(1000, 9999)}"
        segment = random.choice(customer_segments)
        
        # Sales details
        channel = random.choice(sales_channels)
        
        # Base prices by category
        base_prices = {
            'Electronics': (200, 1500),
            'Furniture': (150, 800),
            'Stationery': (10, 100),
            'Software': (50, 500)
        }
        
        unit_price = round(random.uniform(*base_prices[category]), 2)
        
        # Quantity (enterprise customers buy more)
        if segment == 'Enterprise':
            quantity = random.randint(5, 50)
        elif segment == 'SMB':
            quantity = random.randint(2, 20)
        else:
            quantity = random.randint(1, 5)
        
        # Calculate values
        gross_revenue = round(unit_price * quantity * seasonal_factor, 2)
        discount_rate = round(random.uniform(0, 0.15) if segment in ['Enterprise', 'Government'] else random.uniform(0, 0.05), 2)
        discount_amount = round(gross_revenue * discount_rate, 2)
        net_revenue = round(gross_revenue - discount_amount, 2)
        cost = round(net_revenue * random.uniform(0.4, 0.7), 2)
        profit = round(net_revenue - cost, 2)
        
        # Sales rep
        sales_rep = f"Rep_{random.randint(1, 20):02d}"
        
        # Order status
        status = random.choices(
            ['Completed', 'Pending', 'Cancelled'],
            weights=[0.85, 0.10, 0.05]
        )[0]
        
        # Create record
        record = {
            'transaction_id': f"TXN{i+1:06d}",
            'transaction_date': transaction_date.strftime('%Y-%m-%d'),
            'year': transaction_date.year,
            'quarter': f"Q{(month-1)//3 + 1}",
            'month': transaction_date.strftime('%B'),
            'month_num': month,
            'day_of_week': transaction_date.strftime('%A'),
            'customer_id': customer_id,
            'customer_segment': segment,
            'region': region,
            'city': city,
            'product_category': category,
            'product_name': product,
            'quantity': quantity,
            'unit_price': unit_price,
            'gross_revenue': gross_revenue,
            'discount_rate': discount_rate,
            'discount_amount': discount_amount,
            'net_revenue': net_revenue,
            'cost': cost,
            'profit': profit,
            'sales_channel': channel,
            'sales_rep': sales_rep,
            'order_status': status
        }
        
        data.append(record)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add some data quality issues for cleaning demonstration
    # Missing values
    missing_indices = np.random.choice(df.index, size=int(0.02 * len(df)), replace=False)
    df.loc[missing_indices, 'sales_rep'] = np.nan
    
    # Duplicates
    duplicate_rows = df.sample(n=int(0.01 * len(df)))
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    print(f"✓ Generated {len(df)} records")
    print(f"✓ Date range: {df['transaction_date'].min()} to {df['transaction_date'].max()}")
    print(f"✓ Total revenue: £{df['net_revenue'].sum():,.2f}")
    
    return df

def save_data(df, filename='sales_data_raw.csv'):
    """Save generated data to CSV"""
    filepath = f'data/raw/{filename}'
    df.to_csv(filepath, index=False)
    print(f"\n✓ Data saved to {filepath}")
    
    # Display sample
    print(f"\nSample data (first 5 records):")
    print(df.head())
    
    # Display summary statistics
    print(f"\nData Summary:")
    print(f"Total Records: {len(df)}")
    print(f"Date Range: {df['transaction_date'].min()} to {df['transaction_date'].max()}")
    print(f"Total Net Revenue: £{df['net_revenue'].sum():,.2f}")
    print(f"Total Profit: £{df['profit'].sum():,.2f}")
    print(f"Unique Customers: {df['customer_id'].nunique()}")
    print(f"Unique Products: {df['product_name'].nunique()}")

if __name__ == "__main__":
    # Generate sales data
    sales_df = generate_sales_data(num_records=5000)
    
    # Save to CSV
    save_data(sales_df)
    
    print("\n" + "="*60)
    print("Data generation complete!")
    print("Next step: Run data_cleaning.py to clean and transform the data")
    print("="*60)
