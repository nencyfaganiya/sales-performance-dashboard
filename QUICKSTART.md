# Quick Start Guide

## Getting Started in 5 Minutes

This guide will help you get the Sales Performance Dashboard project up and running quickly.

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/sales-performance-dashboard.git
cd sales-performance-dashboard
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Complete Pipeline
Execute all scripts in sequence to generate data, clean it, calculate KPIs, and create visualizations:

```bash
# Generate sample sales data
python scripts/data_generation.py

# Clean and transform the data
python scripts/data_cleaning.py

# Calculate business KPIs
python scripts/kpi_calculations.py

# Create visualizations
python scripts/visualizations.py
```

### Step 4: View the Results

After running all scripts, you'll have:

**Processed Data**:
- `data/processed/sales_data_cleaned.csv` - Main cleaned dataset
- `data/processed/monthly_summary.csv` - Monthly aggregations
- `data/processed/product_performance.csv` - Product-level metrics
- `data/processed/regional_performance.csv` - Regional analysis
- `data/processed/customer_segment_analysis.csv` - Customer segments

**Analysis Outputs**:
- `data/output/kpi_summary.csv` - All calculated KPIs

**Visualizations**:
- `data/output/revenue_trend.png` - Monthly revenue chart
- `data/output/category_performance.png` - Category comparison
- `data/output/regional_heatmap.png` - Regional performance matrix
- `data/output/customer_segment_distribution.png` - Segment pie chart
- `data/output/top_products.png` - Top 10 products
- `data/output/sales_channel_comparison.png` - Channel analysis
- `data/output/quarterly_trend.png` - Quarterly trends
- `data/output/executive_dashboard.png` - Executive overview



## What You'll See

### Generated Data
- **5,000** sales transactions
- **3 years** of historical data (2022-2024)
- **£24M** in total revenue
- **4 regions**, **20 products**, **3,800+ customers**

### Key Insights Demonstrated
- Revenue trends and seasonality patterns
- Product category performance comparison
- Regional sales distribution
- Customer segmentation analysis
- Top performing products and customers
- Sales channel effectiveness
- Quarter-over-quarter growth analysis
