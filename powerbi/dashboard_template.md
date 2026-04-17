# Power BI Dashboard Template

## Overview
This document provides specifications for creating a comprehensive Power BI dashboard using the processed sales data.

## Data Sources

### Primary Data Table
**File**: `data/processed/sales_data_cleaned.csv`

**Key Fields**:
- `transaction_id` (Text) - Unique identifier
- `transaction_date` (Date) - Date of transaction
- `year`, `quarter`, `month` (Text) - Time dimensions
- `customer_id`, `customer_segment` (Text) - Customer dimensions
- `region`, `city` (Text) - Geographic dimensions
- `product_category`, `product_name` (Text) - Product dimensions
- `net_revenue`, `profit`, `cost` (Currency) - Financial metrics
- `quantity` (Whole Number) - Units sold
- `profit_margin` (Decimal) - Calculated percentage
- `sales_channel`, `sales_rep` (Text) - Sales dimensions
- `order_status` (Text) - Status dimension

### Supporting Tables
1. **Monthly Summary**: `data/processed/monthly_summary.csv`
2. **Product Performance**: `data/processed/product_performance.csv`
3. **Regional Performance**: `data/processed/regional_performance.csv`
4. **Customer Segment Analysis**: `data/processed/customer_segment_analysis.csv`

## Dashboard Structure

### Page 1: Executive Overview
**Purpose**: High-level business performance at a glance

**Visualizations**:
1. **KPI Cards** (Top Row)
   - Total Revenue (Card visual)
   - Total Profit (Card visual)
   - Profit Margin % (Card visual)
   - Total Transactions (Card visual)
   - Average Order Value (Card visual)
   - Unique Customers (Card visual)

2. **Revenue Trend** (Line Chart)
   - X-axis: Month/Quarter
   - Y-axis: Net Revenue
   - Add trend line
   - Optional: Forecast for next period

3. **Revenue Mix** (Donut Chart)
   - Values: Net Revenue
   - Legend: Product Category
   - Show percentage labels

4. **Regional Performance** (Map Visual)
   - Location: City/Region
   - Size: Net Revenue
   - Color: Profit Margin %

**Filters Panel**:
- Date Range Slicer
- Customer Segment
- Region
- Product Category

---

### Page 2: Sales Analysis
**Purpose**: Detailed sales performance breakdown

**Visualizations**:
1. **Sales Trend with Comparison** (Line and Clustered Column)
   - X-axis: Month
   - Lines: Current Year Revenue, Previous Year Revenue
   - Show YoY growth %

2. **Product Category Performance** (Stacked Bar Chart)
   - Y-axis: Product Category
   - X-axis: Revenue and Profit (stacked)
   - Data labels on bars

3. **Sales Channel Distribution** (Clustered Column Chart)
   - X-axis: Sales Channel
   - Y-axis: Revenue
   - Color: Customer Segment

4. **Top 10 Products Table** (Table Visual)
   - Columns: Product Name, Category, Revenue, Profit, Units Sold, Profit Margin %
   - Conditional formatting on Profit Margin
   - Sort by Revenue descending

**Filters**:
- Date Range
- Region
- Sales Channel

---

### Page 3: Customer Insights
**Purpose**: Customer behavior and segmentation analysis

**Visualizations**:
1. **Customer Segment Analysis** (Pie Chart)
   - Values: Revenue
   - Legend: Customer Segment
   - Show percentages

2. **Customer Acquisition Trend** (Area Chart)
   - X-axis: Month
   - Y-axis: New Customers Count
   - Fill area with gradient

3. **Revenue Per Customer** (Clustered Bar)
   - Y-axis: Customer Segment
   - X-axis: Avg Revenue Per Customer
   - Sort descending

4. **Repeat Customer Analysis** (KPI Cards)
   - Total Customers
   - Repeat Customers
   - Repeat Rate %
   - Average Purchases Per Customer

5. **Top 20 Customers Table**
   - Customer ID, Total Revenue, Total Transactions, Avg Order Value
   - Conditional formatting

**Filters**:
- Date Range
- Customer Segment
- Region

---

### Page 4: Geographic Performance
**Purpose**: Regional and city-level analysis

**Visualizations**:
1. **Regional Comparison** (Map)
   - Location: Region
   - Bubble Size: Revenue
   - Bubble Color: Profit Margin %

2. **Revenue by Region** (Clustered Column)
   - X-axis: Region
   - Y-axis: Revenue
   - Color by: Year (for comparison)

3. **City Performance Matrix** (Matrix Visual)
   - Rows: Region > City
   - Values: Revenue, Profit, Transactions
   - Conditional formatting with data bars

4. **Regional Trends** (Line Chart)
   - X-axis: Month
   - Y-axis: Revenue
   - Legend: Region (multiple lines)

**Filters**:
- Date Range
- Region (multi-select)

---

## DAX Measures

### Revenue Metrics
```DAX
Total Revenue = SUM(Sales[net_revenue])

Total Profit = SUM(Sales[profit])

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0) * 100

Average Order Value = AVERAGE(Sales[net_revenue])

YoY Revenue Growth % = 
VAR CurrentYearRevenue = [Total Revenue]
VAR PreviousYearRevenue = 
    CALCULATE(
        [Total Revenue],
        SAMEPERIODLASTYEAR('Date'[Date])
    )
RETURN
    DIVIDE(CurrentYearRevenue - PreviousYearRevenue, PreviousYearRevenue, 0) * 100

MoM Revenue Growth % = 
VAR CurrentMonthRevenue = [Total Revenue]
VAR PreviousMonthRevenue = 
    CALCULATE(
        [Total Revenue],
        DATEADD('Date'[Date], -1, MONTH)
    )
RETURN
    DIVIDE(CurrentMonthRevenue - PreviousMonthRevenue, PreviousMonthRevenue, 0) * 100
```

### Customer Metrics
```DAX
Total Customers = DISTINCTCOUNT(Sales[customer_id])

New Customers = 
CALCULATE(
    DISTINCTCOUNT(Sales[customer_id]),
    FILTER(
        Sales,
        Sales[transaction_date] = 
            CALCULATE(
                MIN(Sales[transaction_date]),
                ALLEXCEPT(Sales, Sales[customer_id])
            )
    )
)

Repeat Customers = 
CALCULATE(
    DISTINCTCOUNT(Sales[customer_id]),
    FILTER(
        VALUES(Sales[customer_id]),
        CALCULATE(COUNTROWS(Sales)) > 1
    )
)

Repeat Rate % = DIVIDE([Repeat Customers], [Total Customers], 0) * 100

Customer Lifetime Value = 
AVERAGEX(
    VALUES(Sales[customer_id]),
    CALCULATE(SUM(Sales[net_revenue]))
)
```

### Operational Metrics
```DAX
Total Transactions = COUNTROWS(Sales)

Total Units Sold = SUM(Sales[quantity])

Average Discount % = AVERAGE(Sales[discount_rate]) * 100

Completion Rate % = 
DIVIDE(
    CALCULATE(COUNTROWS(Sales), Sales[order_status] = "Completed"),
    COUNTROWS(Sales),
    0
) * 100
```

## Color Scheme (Brand Consistent)
- Primary: `#0078D4` (Blue) - Revenue/Main metrics
- Secondary: `#107C10` (Green) - Profit/Positive growth
- Accent: `#D83B01` (Orange) - Alerts/Declining metrics
- Neutral: `#605E5C` (Gray) - Supporting text
- Background: `#FFFFFF` (White)

## Design Guidelines

### Typography
- **Titles**: Segoe UI, 18pt, Bold
- **Subtitles**: Segoe UI, 14pt, Semibold
- **Body Text**: Segoe UI, 11pt, Regular
- **Data Labels**: Segoe UI, 10pt, Regular

### Layout
- Maintain consistent padding (10px minimum)
- Use 12-column grid for alignment
- Group related visuals with subtle borders
- Use white space effectively

### Interactivity
- Enable cross-filtering between all visuals
- Add drill-down capability on time dimensions
- Include tooltips with additional context
- Add bookmarks for different views

## Data Refresh Strategy
- Schedule: Daily at 6:00 AM
- Incremental refresh: Load last 30 days, keep 24 months
- Error handling: Send email notification on failure

## Testing Checklist
- [ ] All measures calculate correctly
- [ ] Filters work across all pages
- [ ] Cross-filtering is enabled
- [ ] Mobile layout is responsive
- [ ] Performance is under 3 seconds load time
- [ ] All visualizations have titles
- [ ] Data labels are readable
- [ ] Color blind friendly palette used

## Export and Sharing
- Publish to Power BI Service
- Create App workspace
- Set up Row-Level Security if needed
- Enable export to Excel for tables
- Configure automatic email subscriptions

---

## Notes
- All currency values should display with £ symbol
- Percentages should show 2 decimal places
- Large numbers use K/M notation (e.g., £1.5M)
- Dates in DD/MM/YYYY format for UK audience
