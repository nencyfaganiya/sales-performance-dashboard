"""
Data Visualization Script
Create professional charts and graphs for BI reporting
Author: Nency Faganiya
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for professional-looking charts
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_data():
    """Load processed data"""
    print("Loading data for visualization...")
    df = pd.read_csv('data/processed/sales_data_cleaned.csv')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    print(f"✓ Loaded {len(df)} records\n")
    return df

def create_revenue_trend_chart(df):
    """Create revenue trend over time"""
    print("Creating revenue trend chart...")
    
    # Monthly revenue
    monthly_revenue = df.groupby(df['transaction_date'].dt.to_period('M'))['net_revenue'].sum()
    monthly_revenue.index = monthly_revenue.index.to_timestamp()
    
    plt.figure(figsize=(14, 6))
    plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o', linewidth=2, markersize=6)
    plt.title('Monthly Revenue Trend', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Revenue (£)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Format y-axis to show currency
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'£{x/1000:.0f}K'))
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('data/output/revenue_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: revenue_trend.png")

def create_category_performance_chart(df):
    """Create product category performance chart"""
    print("Creating category performance chart...")
    
    # Category performance
    category_perf = df.groupby('product_category').agg({
        'net_revenue': 'sum',
        'profit': 'sum'
    }).sort_values('net_revenue', ascending=True)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(category_perf))
    width = 0.35
    
    bars1 = ax.barh(x - width/2, category_perf['net_revenue'], width, label='Revenue', alpha=0.8)
    bars2 = ax.barh(x + width/2, category_perf['profit'], width, label='Profit', alpha=0.8)
    
    ax.set_xlabel('Amount (£)', fontsize=12)
    ax.set_title('Product Category Performance', fontsize=16, fontweight='bold', pad=20)
    ax.set_yticks(x)
    ax.set_yticklabels(category_perf.index)
    ax.legend()
    
    # Format x-axis
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'£{x/1000:.0f}K'))
    
    plt.tight_layout()
    plt.savefig('data/output/category_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: category_performance.png")

def create_regional_heatmap(df):
    """Create regional performance heatmap"""
    print("Creating regional performance heatmap...")
    
    # Pivot table for heatmap
    regional_pivot = df.pivot_table(
        values='net_revenue',
        index='region',
        columns='product_category',
        aggfunc='sum',
        fill_value=0
    )
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(regional_pivot, annot=True, fmt='.0f', cmap='YlOrRd', 
                cbar_kws={'label': 'Revenue (£)'})
    plt.title('Revenue by Region and Category', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Product Category', fontsize=12)
    plt.ylabel('Region', fontsize=12)
    plt.tight_layout()
    plt.savefig('data/output/regional_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: regional_heatmap.png")

def create_customer_segment_pie(df):
    """Create customer segment distribution pie chart"""
    print("Creating customer segment distribution chart...")
    
    segment_revenue = df.groupby('customer_segment')['net_revenue'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 8))
    colors = sns.color_palette('pastel')
    explode = [0.05] + [0] * (len(segment_revenue) - 1)  # Explode the largest segment
    
    plt.pie(segment_revenue.values, labels=segment_revenue.index, autopct='%1.1f%%',
            startangle=90, colors=colors, explode=explode)
    plt.title('Revenue Distribution by Customer Segment', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('data/output/customer_segment_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: customer_segment_distribution.png")

def create_top_products_chart(df):
    """Create top 10 products chart"""
    print("Creating top products chart...")
    
    top_products = df.groupby('product_name')['net_revenue'].sum().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(12, 8))
    bars = plt.barh(range(len(top_products)), top_products.values, alpha=0.8)
    
    # Color gradient
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(top_products)))
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    
    plt.yticks(range(len(top_products)), top_products.index)
    plt.xlabel('Revenue (£)', fontsize=12)
    plt.title('Top 10 Products by Revenue', fontsize=16, fontweight='bold', pad=20)
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'£{x/1000:.0f}K'))
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('data/output/top_products.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: top_products.png")

def create_sales_channel_comparison(df):
    """Create sales channel comparison"""
    print("Creating sales channel comparison chart...")
    
    channel_metrics = df.groupby('sales_channel').agg({
        'net_revenue': 'sum',
        'transaction_id': 'count',
        'profit': 'sum'
    }).round(2)
    channel_metrics.columns = ['Revenue', 'Transactions', 'Profit']
    channel_metrics['Avg_Transaction_Value'] = (channel_metrics['Revenue'] / channel_metrics['Transactions']).round(2)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Sales Channel Performance Analysis', fontsize=16, fontweight='bold')
    
    # Revenue by channel
    axes[0, 0].bar(channel_metrics.index, channel_metrics['Revenue'], alpha=0.8)
    axes[0, 0].set_title('Revenue by Channel')
    axes[0, 0].set_ylabel('Revenue (£)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Transactions by channel
    axes[0, 1].bar(channel_metrics.index, channel_metrics['Transactions'], alpha=0.8, color='coral')
    axes[0, 1].set_title('Transactions by Channel')
    axes[0, 1].set_ylabel('Number of Transactions')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Profit by channel
    axes[1, 0].bar(channel_metrics.index, channel_metrics['Profit'], alpha=0.8, color='lightgreen')
    axes[1, 0].set_title('Profit by Channel')
    axes[1, 0].set_ylabel('Profit (£)')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # Avg transaction value by channel
    axes[1, 1].bar(channel_metrics.index, channel_metrics['Avg_Transaction_Value'], alpha=0.8, color='mediumpurple')
    axes[1, 1].set_title('Avg Transaction Value by Channel')
    axes[1, 1].set_ylabel('Avg Value (£)')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('data/output/sales_channel_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: sales_channel_comparison.png")

def create_quarterly_trend_chart(df):
    """Create quarterly trend comparison"""
    print("Creating quarterly trend chart...")
    
    quarterly = df.groupby(['year', 'quarter']).agg({
        'net_revenue': 'sum',
        'profit': 'sum'
    }).reset_index()
    quarterly['period'] = quarterly['year'].astype(str) + ' ' + quarterly['quarter']
    
    fig, ax1 = plt.subplots(figsize=(14, 6))
    
    x = range(len(quarterly))
    ax1.plot(x, quarterly['net_revenue'], marker='o', linewidth=2, markersize=8, 
             label='Revenue', color='steelblue')
    ax1.set_xlabel('Quarter', fontsize=12)
    ax1.set_ylabel('Revenue (£)', fontsize=12, color='steelblue')
    ax1.tick_params(axis='y', labelcolor='steelblue')
    
    ax2 = ax1.twinx()
    ax2.plot(x, quarterly['profit'], marker='s', linewidth=2, markersize=8, 
             label='Profit', color='darkgreen')
    ax2.set_ylabel('Profit (£)', fontsize=12, color='darkgreen')
    ax2.tick_params(axis='y', labelcolor='darkgreen')
    
    plt.title('Quarterly Revenue and Profit Trend', fontsize=16, fontweight='bold', pad=20)
    ax1.set_xticks(x)
    ax1.set_xticklabels(quarterly['period'], rotation=45, ha='right')
    ax1.grid(True, alpha=0.3)
    
    # Add legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    plt.tight_layout()
    plt.savefig('data/output/quarterly_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: quarterly_trend.png")

def create_executive_dashboard(df):
    """Create comprehensive executive dashboard"""
    print("Creating executive dashboard...")
    
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # KPI Cards (Top Row)
    total_revenue = df['net_revenue'].sum()
    total_profit = df['profit'].sum()
    total_transactions = len(df)
    avg_order_value = df['net_revenue'].mean()
    
    # KPI 1: Total Revenue
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.text(0.5, 0.5, f'£{total_revenue/1e6:.2f}M', ha='center', va='center', 
             fontsize=24, fontweight='bold', color='steelblue')
    ax1.text(0.5, 0.2, 'Total Revenue', ha='center', va='center', fontsize=12)
    ax1.axis('off')
    ax1.set_facecolor('#f0f0f0')
    
    # KPI 2: Total Profit
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.text(0.5, 0.5, f'£{total_profit/1e6:.2f}M', ha='center', va='center', 
             fontsize=24, fontweight='bold', color='darkgreen')
    ax2.text(0.5, 0.2, 'Total Profit', ha='center', va='center', fontsize=12)
    ax2.axis('off')
    ax2.set_facecolor('#f0f0f0')
    
    # KPI 3: Total Transactions
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.text(0.5, 0.5, f'{total_transactions:,}', ha='center', va='center', 
             fontsize=24, fontweight='bold', color='coral')
    ax3.text(0.5, 0.2, 'Transactions', ha='center', va='center', fontsize=12)
    ax3.axis('off')
    ax3.set_facecolor('#f0f0f0')
    
    # Monthly trend (Middle Left)
    ax4 = fig.add_subplot(gs[1, :2])
    monthly_revenue = df.groupby(df['transaction_date'].dt.to_period('M'))['net_revenue'].sum()
    monthly_revenue.index = monthly_revenue.index.to_timestamp()
    ax4.plot(monthly_revenue.index, monthly_revenue.values, marker='o', linewidth=2)
    ax4.set_title('Monthly Revenue Trend', fontweight='bold')
    ax4.tick_params(axis='x', rotation=45)
    ax4.grid(True, alpha=0.3)
    
    # Category breakdown (Middle Right)
    ax5 = fig.add_subplot(gs[1, 2])
    category_revenue = df.groupby('product_category')['net_revenue'].sum()
    ax5.pie(category_revenue.values, labels=category_revenue.index, autopct='%1.0f%%', startangle=90)
    ax5.set_title('Category Mix', fontweight='bold')
    
    # Regional performance (Bottom Left)
    ax6 = fig.add_subplot(gs[2, :2])
    regional = df.groupby('region')['net_revenue'].sum().sort_values()
    ax6.barh(regional.index, regional.values, alpha=0.8)
    ax6.set_title('Revenue by Region', fontweight='bold')
    ax6.set_xlabel('Revenue (£)')
    
    # Segment performance (Bottom Right)
    ax7 = fig.add_subplot(gs[2, 2])
    segment = df.groupby('customer_segment')['net_revenue'].sum().sort_values()
    ax7.barh(segment.index, segment.values, alpha=0.8, color='mediumpurple')
    ax7.set_title('Segment Revenue', fontweight='bold')
    ax7.set_xlabel('Revenue (£)')
    
    fig.suptitle('Executive Sales Dashboard', fontsize=18, fontweight='bold', y=0.98)
    
    plt.savefig('data/output/executive_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Saved: executive_dashboard.png")

if __name__ == "__main__":
    # Load data
    df = load_data()
    
    print("="*60)
    print("GENERATING VISUALIZATIONS")
    print("="*60 + "\n")
    
    # Create all visualizations
    create_revenue_trend_chart(df)
    create_category_performance_chart(df)
    create_regional_heatmap(df)
    create_customer_segment_pie(df)
    create_top_products_chart(df)
    create_sales_channel_comparison(df)
    create_quarterly_trend_chart(df)
    create_executive_dashboard(df)
    
    print("\n" + "="*60)
    print("All visualizations created successfully!")
    print("Charts saved in data/output/ directory")
    print("="*60)
