# 📊 Sales Performance Dashboard - BI Analytics Project

A comprehensive Business Intelligence solution demonstrating end-to-end data analytics capabilities, from data extraction and transformation to interactive visualization and insights generation.

## 🎯 Project Overview

This project showcases a complete BI workflow for analyzing sales performance data, featuring:
- **Data Generation & Cleaning**: Python-based synthetic data creation with realistic business scenarios
- **ETL Pipeline**: Automated data transformation and quality checks
- **Advanced Analytics**: KPI calculations, trend analysis, and predictive insights
- **Interactive Dashboards**: Power BI compatible data models and visualizations
- **Automated Reporting**: Python scripts for generating executive summaries

## 🛠️ Technical Stack

- **Python**: Pandas, NumPy, Matplotlib, Seaborn
- **Data Storage**: CSV, SQL-ready formats
- **Visualization**: Power BI (PBIX template included), Python plotting
- **Version Control**: Git/GitHub
- **Documentation**: Markdown, Jupyter Notebooks

## 📁 Project Structure

```
sales-performance-dashboard/
├── data/
│   ├── raw/                    # Original data files
│   ├── processed/              # Cleaned and transformed data
│   └── output/                 # Analysis results and reports
├── scripts/
│   ├── data_generation.py      # Generate synthetic sales data
│   ├── data_cleaning.py        # Data quality and transformation
│   ├── kpi_calculations.py     # Business metrics and KPIs
│   └── visualizations.py       # Charts and graphs generation
├── notebooks/
│   └── exploratory_analysis.ipynb  # Interactive data exploration
├── powerbi/
│   └── dashboard_template.md   # Power BI dashboard specifications
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip install -r requirements.txt
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/sales-performance-dashboard.git
cd sales-performance-dashboard

# Install dependencies
pip install -r requirements.txt
```

### Usage

1. **Generate Sample Data**
```bash
python scripts/data_generation.py
```

2. **Clean and Transform Data**
```bash
python scripts/data_cleaning.py
```

3. **Calculate KPIs**
```bash
python scripts/kpi_calculations.py
```

4. **Generate Visualizations**
```bash
python scripts/visualizations.py
```

## 📈 Key Features

### Data Analysis
- **Sales Trends**: Month-over-month, quarter-over-quarter analysis
- **Customer Segmentation**: RFM analysis and cohort grouping
- **Product Performance**: Revenue contribution and growth rates
- **Regional Analysis**: Geographic performance comparison

### KPIs Tracked
- Total Revenue & Revenue Growth Rate
- Average Order Value (AOV)
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (CLV)
- Sales Conversion Rate
- Top Performing Products/Regions

### Visualizations
- Revenue trend lines with forecasting
- Product category performance bars
- Regional heatmaps
- Customer segmentation scatter plots
- Executive summary dashboards

## 📊 Power BI Dashboard

The Power BI dashboard includes:
- **Executive Overview**: High-level KPIs and trends
- **Sales Analysis**: Detailed breakdowns by product, region, and time
- **Customer Insights**: Segmentation and behavior patterns
- **Performance Metrics**: Target vs. actual comparisons

*Note: Import the processed data from `data/processed/` into Power BI using the specifications in `powerbi/dashboard_template.md`*

## 🔍 Sample Insights

This project demonstrates ability to:
- Identify sales trends and seasonal patterns
- Spot underperforming products or regions
- Calculate customer retention metrics
- Provide actionable recommendations based on data
- Create executive-ready reports and visualizations

## 🤝 Contributing

Suggestions and improvements are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Submit pull requests with enhancements
- Share feedback on the analysis approach
