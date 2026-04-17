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

### Step 5: Import to Power BI (Optional)

1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Navigate to `data/processed/sales_data_cleaned.csv`
4. Load the data
5. Follow the specifications in `powerbi/dashboard_template.md` to create your dashboard

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

## Customization

### Change Data Volume
Edit `scripts/data_generation.py`:
```python
sales_df = generate_sales_data(num_records=10000)  # Default is 5000
```

### Adjust Date Range
```python
sales_df = generate_sales_data(
    num_records=5000,
    start_date='2020-01-01',
    end_date='2024-12-31'
)
```

### Modify Product Categories
Edit the `products` dictionary in `data_generation.py`:
```python
products = {
    'Your Category': ['Product 1', 'Product 2', ...],
    # Add more categories
}
```

## Troubleshooting

### Import Error: No module named 'pandas'
```bash
pip install pandas numpy matplotlib seaborn
```

### Visualization Not Showing
Ensure matplotlib backend is properly configured. If running on a server, visualizations are saved as files (not displayed).

### Permission Denied Error
Make sure you have write permissions in the project directory.

## Next Steps

1. **Explore the Data**: Open CSV files to understand the data structure
2. **Analyze KPIs**: Review the KPI summary for key metrics
3. **Study Visualizations**: Look at the generated charts in `data/output/`
4. **Build Power BI Dashboard**: Use the template guide to create interactive dashboards
5. **Customize**: Modify scripts to match your specific business needs

## Learn More

- See `README.md` for comprehensive project documentation
- Check `powerbi/dashboard_template.md` for Power BI specifications
- Review individual Python scripts for detailed comments and logic

---

**Time to Complete**: ~5 minutes
**Output**: Fully functional BI analytics project with data, KPIs, and visualizations ready for presentation or further analysis.
