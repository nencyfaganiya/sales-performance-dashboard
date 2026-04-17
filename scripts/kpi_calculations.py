"""
KPI Calculations Script
Calculate key performance indicators and business metrics
Author: Nency Faganiya
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_cleaned_data():
    """Load cleaned sales data"""
    print("Loading cleaned data...")
    df = pd.read_csv('data/processed/sales_data_cleaned.csv')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    print(f"✓ Loaded {len(df)} records\n")
    return df

def calculate_revenue_kpis(df):
    """Calculate revenue-related KPIs"""
    print("="*60)
    print("REVENUE KPIs")
    print("="*60)
    
    kpis = {}
    
    # Total Revenue
    kpis['total_revenue'] = df['net_revenue'].sum()
    print(f"Total Revenue: £{kpis['total_revenue']:,.2f}")
    
    # Total Profit
    kpis['total_profit'] = df['profit'].sum()
    print(f"Total Profit: £{kpis['total_profit']:,.2f}")
    
    # Average Profit Margin
    kpis['avg_profit_margin'] = (kpis['total_profit'] / kpis['total_revenue'] * 100)
    print(f"Average Profit Margin: {kpis['avg_profit_margin']:.2f}%")
    
    # Average Order Value (AOV)
    kpis['avg_order_value'] = df['net_revenue'].mean()
    print(f"Average Order Value: £{kpis['avg_order_value']:,.2f}")
    
    # Revenue Growth Rate (Year over Year)
    yearly_revenue = df.groupby('year')['net_revenue'].sum()
    if len(yearly_revenue) > 1:
        revenue_growth = ((yearly_revenue.iloc[-1] - yearly_revenue.iloc[-2]) / yearly_revenue.iloc[-2] * 100)
        kpis['yoy_revenue_growth'] = revenue_growth
        print(f"YoY Revenue Growth: {revenue_growth:.2f}%")
    
    return kpis

def calculate_customer_kpis(df):
    """Calculate customer-related KPIs"""
    print("\n" + "="*60)
    print("CUSTOMER KPIs")
    print("="*60)
    
    kpis = {}
    
    # Total Customers
    kpis['total_customers'] = df['customer_id'].nunique()
    print(f"Total Unique Customers: {kpis['total_customers']:,}")
    
    # Customer Lifetime Value (CLV) - Simplified
    customer_revenue = df.groupby('customer_id')['net_revenue'].sum()
    kpis['avg_clv'] = customer_revenue.mean()
    print(f"Average Customer Lifetime Value: £{kpis['avg_clv']:,.2f}")
    
    # Average Revenue Per Customer
    kpis['revenue_per_customer'] = df['net_revenue'].sum() / kpis['total_customers']
    print(f"Revenue Per Customer: £{kpis['revenue_per_customer']:,.2f}")
    
    # Repeat Customer Rate
    customer_purchases = df.groupby('customer_id')['transaction_id'].count()
    repeat_customers = (customer_purchases > 1).sum()
    kpis['repeat_customer_rate'] = (repeat_customers / kpis['total_customers'] * 100)
    print(f"Repeat Customer Rate: {kpis['repeat_customer_rate']:.2f}%")
    
    # Average Purchases Per Customer
    kpis['avg_purchases_per_customer'] = customer_purchases.mean()
    print(f"Average Purchases Per Customer: {kpis['avg_purchases_per_customer']:.2f}")
    
    return kpis

def calculate_operational_kpis(df):
    """Calculate operational KPIs"""
    print("\n" + "="*60)
    print("OPERATIONAL KPIs")
    print("="*60)
    
    kpis = {}
    
    # Total Transactions
    kpis['total_transactions'] = len(df)
    print(f"Total Transactions: {kpis['total_transactions']:,}")
    
    # Order Completion Rate
    completed_orders = df[df['order_status'] == 'Completed'].shape[0]
    kpis['order_completion_rate'] = (completed_orders / kpis['total_transactions'] * 100)
    print(f"Order Completion Rate: {kpis['order_completion_rate']:.2f}%")
    
    # Average Discount Rate
    kpis['avg_discount_rate'] = (df['discount_rate'].mean() * 100)
    print(f"Average Discount Rate: {kpis['avg_discount_rate']:.2f}%")
    
    # Units Sold
    kpis['total_units_sold'] = df['quantity'].sum()
    print(f"Total Units Sold: {kpis['total_units_sold']:,}")
    
    # Average Units Per Transaction
    kpis['avg_units_per_transaction'] = df['quantity'].mean()
    print(f"Average Units Per Transaction: {kpis['avg_units_per_transaction']:.2f}")
    
    return kpis

def calculate_segment_kpis(df):
    """Calculate segment-specific KPIs"""
    print("\n" + "="*60)
    print("SEGMENT PERFORMANCE")
    print("="*60)
    
    # By Customer Segment
    print("\nBy Customer Segment:")
    segment_kpis = df.groupby('customer_segment').agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'transaction_id': 'count'
    }).round(2)
    segment_kpis.columns = ['Revenue', 'Profit', 'Transactions']
    segment_kpis['Profit_Margin_%'] = (segment_kpis['Profit'] / segment_kpis['Revenue'] * 100).round(2)
    print(segment_kpis)
    
    # By Region
    print("\nBy Region:")
    region_kpis = df.groupby('region').agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'transaction_id': 'count'
    }).round(2)
    region_kpis.columns = ['Revenue', 'Profit', 'Transactions']
    region_kpis['Profit_Margin_%'] = (region_kpis['Profit'] / region_kpis['Revenue'] * 100).round(2)
    print(region_kpis)
    
    # By Product Category
    print("\nBy Product Category:")
    category_kpis = df.groupby('product_category').agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'quantity': 'sum'
    }).round(2)
    category_kpis.columns = ['Revenue', 'Profit', 'Units_Sold']
    category_kpis['Profit_Margin_%'] = (category_kpis['Profit'] / category_kpis['Revenue'] * 100).round(2)
    print(category_kpis)
    
    return segment_kpis, region_kpis, category_kpis

def calculate_time_based_kpis(df):
    """Calculate time-based trends"""
    print("\n" + "="*60)
    print("TIME-BASED TRENDS")
    print("="*60)
    
    # Monthly trends
    monthly = df.groupby(['year', 'month_num', 'month']).agg({
        'net_revenue': 'sum',
        'profit': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    monthly.columns = ['Year', 'Month_Num', 'Month', 'Revenue', 'Profit', 'Transactions']
    
    # Calculate month-over-month growth
    monthly['Revenue_MoM_Growth_%'] = monthly['Revenue'].pct_change() * 100
    monthly['Transactions_MoM_Growth_%'] = monthly['Transactions'].pct_change() * 100
    
    print("\nMonthly Revenue Trend (Last 6 Months):")
    print(monthly[['Year', 'Month', 'Revenue', 'Revenue_MoM_Growth_%']].tail(6))
    
    # Quarterly trends
    quarterly = df.groupby(['year', 'quarter']).agg({
        'net_revenue': 'sum',
        'profit': 'sum'
    }).reset_index()
    quarterly.columns = ['Year', 'Quarter', 'Revenue', 'Profit']
    quarterly['Revenue_QoQ_Growth_%'] = quarterly['Revenue'].pct_change() * 100
    
    print("\nQuarterly Performance:")
    print(quarterly)
    
    return monthly, quarterly

def identify_top_performers(df):
    """Identify top performing elements"""
    print("\n" + "="*60)
    print("TOP PERFORMERS")
    print("="*60)
    
    # Top 10 Products by Revenue
    print("\nTop 10 Products by Revenue:")
    top_products = df.groupby('product_name')['net_revenue'].sum().sort_values(ascending=False).head(10)
    print(top_products)
    
    # Top 10 Customers by Revenue
    print("\nTop 10 Customers by Revenue:")
    top_customers = df.groupby('customer_id')['net_revenue'].sum().sort_values(ascending=False).head(10)
    print(top_customers)
    
    # Top Sales Reps
    print("\nTop 10 Sales Representatives:")
    top_reps = df.groupby('sales_rep')['net_revenue'].sum().sort_values(ascending=False).head(10)
    print(top_reps)
    
    # Top Cities by Revenue
    print("\nTop 10 Cities by Revenue:")
    top_cities = df.groupby('city')['net_revenue'].sum().sort_values(ascending=False).head(10)
    print(top_cities)
    
    return top_products, top_customers, top_reps, top_cities

def save_kpi_summary(all_kpis):
    """Save KPI summary to file"""
    # Create a comprehensive KPI report
    kpi_df = pd.DataFrame(list(all_kpis.items()), columns=['KPI', 'Value'])
    kpi_df.to_csv('data/output/kpi_summary.csv', index=False)
    print(f"\n✓ KPI summary saved to data/output/kpi_summary.csv")

if __name__ == "__main__":
    # Load data
    df = load_cleaned_data()
    
    # Calculate all KPIs
    revenue_kpis = calculate_revenue_kpis(df)
    customer_kpis = calculate_customer_kpis(df)
    operational_kpis = calculate_operational_kpis(df)
    
    # Combine all KPIs
    all_kpis = {**revenue_kpis, **customer_kpis, **operational_kpis}
    
    # Segment analysis
    segment_kpis, region_kpis, category_kpis = calculate_segment_kpis(df)
    
    # Time-based analysis
    monthly, quarterly = calculate_time_based_kpis(df)
    
    # Top performers
    top_products, top_customers, top_reps, top_cities = identify_top_performers(df)
    
    # Save results
    save_kpi_summary(all_kpis)
    
    print("\n" + "="*60)
    print("KPI calculations complete!")
    print("Next step: Run visualizations.py to create charts and graphs")
    print("="*60)
