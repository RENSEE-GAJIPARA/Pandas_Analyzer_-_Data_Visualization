# 📊 Superstore Sales Analyzer & Data Visualization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-0.x-4c72b0)
![License](https://img.shields.io/badge/License-Educational-green)

> A comprehensive, menu-driven Python application for end-to-end sales data analysis and visualization, built on the **Kaggle Superstore Sales Dataset**. Covers data loading, cleaning, statistical analysis, aggregation, pivot tables, and 10 different chart types.


---

## 📌 Project Overview

This project implements a `SalesDataAnalyzer` class that encapsulates the full data analysis pipeline — from loading raw CSV data to generating publication-ready charts. Built using **Object-Oriented Programming (OOP)** principles, it exposes an interactive console menu that guides users through every stage of the analysis.

The project uses the **Superstore Sales Dataset** (9,994 rows × 21 columns) — a real-world retail dataset covering orders across the United States from 2015 to 2018.

---

## 📁 Dataset — Superstore Sales

| Property | Detail |
|---|---|
| **Source** | [Kaggle — Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| **Rows** | 9,994 |
| **Columns** | 21 |
| **Date Range** | 2015 – 2018 |

### Key Columns Used

| Column | Type | Description |
|---|---|---|
| `Order Date` | Date | Date of the order |
| `Ship Date` | Date | Date of shipment |
| `Region` | String | US region (East, West, Central, South) |
| `Segment` | String | Customer segment (Consumer, Corporate, Home Office) |
| `Category` | String | Product category |
| `Sub-Category` | String | Product sub-category |
| `Product Name` | String | Full product name |
| `Sales` | Float | Revenue per order line |
| `Quantity` | Int | Units sold |
| `Discount` | Float | Discount applied (0–1) |
| `Profit` | Float | Profit per order line |
| `State / City` | String | Geographic detail |

> The script also auto-derives `Year`, `Month`, and `Month_Name` columns on load.

---

## 🚀 Features

### Data Operations
| # | Feature | Description |
|---|---|---|
| 1 | **Load Dataset** | Load CSV with auto date parsing and column derivation |
| 2 | **Explore Data** | head, tail, dtypes, column names, shape + info |
| 3 | **Handle Missing Data** | Display, fill with mean, drop, or replace missing values |
| 4 | **Math Operations** | sum, mean, median, std, variance, min, max, percentiles via NumPy |
| 5 | **Split Data** | Split DataFrame by Region, Category, Segment, or Year |
| 6 | **Search / Sort / Filter** | Query by value, sort by column, filter by condition/region/category |
| 7 | **Aggregate Functions** | groupby sum/mean/count on Sales, Profit, Quantity |
| 8 | **Statistical Analysis** | describe() + variance, std, percentiles, skewness |
| 9 | **Pivot Tables** | Region × Category, Year × Segment, or custom pivot |

### Visualizations (10 chart types)
| # | Chart | Description |
|---|---|---|
| 1 | Bar Plot | Total Sales by Region |
| 2 | Bar Plot | Total Profit by Category (green/red coloured) |
| 3 | Line Plot | Monthly Sales Trend over time |
| 4 | Scatter Plot | Sales vs Profit, coloured by Discount |
| 5 | Pie Chart | Sales share by Segment |
| 6 | Histogram | Sales distribution across all orders |
| 7 | Stack Plot | Yearly Sales stacked by Category |
| 8 | Heatmap | Correlation matrix (Seaborn) |
| 9 | Box Plot | Profit distribution by Region (Seaborn) |
| 10 | Subplots | 4-in-1 Sales Dashboard |

---

## 🗂️ Project Structure

```
superstore-analyzer/
│
├── sales_analyzer.py            ← Main application (SalesDataAnalyzer class + menu)
├── Sample - Superstore.csv      ← Kaggle dataset (place here after download)
├── screenshots/                 ← Add your output screenshots here
│   ├── 01_load_dataset.png
│   ├── 02_explore_data.png
│   ├── 03_missing_data.png
│   ├── 04_statistics.png
│   ├── 05_bar_sales_region.png
│   ├── 06_scatter_sales_profit.png
│   ├── 07_monthly_trend.png
│   ├── 08_heatmap.png
│   ├── 09_dashboard.png
│   └── 10_save_visualization.png
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher

### Step 1 — Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 2 — Download the dataset

Download `Sample - Superstore.csv` from Kaggle and place it in the project folder:
🔗 https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

### Step 3 — Run the program

```bash
python sales_analyzer.py
```

---

## ▶️ Program Flow & Usage

```
============================================================
     ====== Data Analysis & Visualization Program ======
============================================================
  1. Load Dataset
  2. Explore Data
  3. Perform DataFrame Operations
  4. Handle Missing Data
  5. Generate Descriptive Statistics
  6. Data Visualization
  7. Save Visualization
  8. Exit
============================================================
Enter your choice:
```

### Recommended workflow for first run

```
1  →  Load Dataset            (enter: Sample - Superstore.csv)
2  →  Explore Data            (try option 1: first 5 rows)
4  →  Handle Missing Data     (try option 1: check for missing values)
5  →  Descriptive Statistics  (full stats on Sales, Profit, Discount, Quantity)
3  →  DataFrame Operations    (try option 4: groupby Region)
6  →  Data Visualization      (try option 10: 4-in-1 Dashboard)
7  →  Save Visualization      (enter: dashboard.png)
8  →  Exit
```

---

## 🏛️ Class Architecture

```
SalesDataAnalyzer
│
├── Class Constants (column name references)
│   ├── DATE_COL, PRODUCT_COL, CATEGORY_COL, SUBCAT_COL
│   ├── REGION_COL, SEGMENT_COL, STATE_COL, CITY_COL
│   └── SALES_COL, PROFIT_COL, DISCOUNT_COL, QTY_COL
│
├── Attributes
│   ├── self.data  →  pd.DataFrame   (loaded dataset)
│   └── self.fig   →  plt.Figure     (last generated plot)
│
└── Methods
    ├── __init__()                  →  Constructor
    ├── __del__()                   →  Destructor (closes all plots)
    ├── load_data(file_path)        →  Load CSV + parse dates + derive columns
    ├── explore_data()              →  head / tail / dtypes / info
    ├── clean_data()                →  Missing value handling
    ├── mathematical_operations()   →  NumPy stats on any column
    ├── combine_data(df)            →  pd.concat with another DataFrame
    ├── split_data()                →  groupby-based DataFrame split
    ├── search_sort_filter()        →  Search, sort, filter rows
    ├── aggregate_functions()       →  groupby sum/mean/count
    ├── statistical_analysis()      →  describe + extra NumPy stats
    ├── create_pivot_table()        →  3 pivot presets + custom pivot
    ├── visualize_data()            →  10 chart types
    └── save_visualization()        →  savefig() to PNG/JPEG
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.8+** | Core language |
| **Pandas** | Data loading, cleaning, groupby, pivot tables |
| **NumPy** | Array operations, mathematical & statistical functions |
| **Matplotlib** | Bar, Line, Scatter, Pie, Histogram, Stack, Subplot charts |
| **Seaborn** | Heatmap, Box plot, enhanced bar plots |
| **OOP** | `SalesDataAnalyzer` class encapsulating all logic |

---

## 💡 Key Insights from the Dataset

- **West** region generates the highest total sales; **South** the lowest.
- **Technology** category has the highest profit margin.
- **Furniture** can yield negative profit on high-discount orders.
- **Consumer** segment accounts for roughly 50% of total sales.
- Higher discounts strongly correlate with lower (or negative) profit — visible in the scatter plot.

---


## 👤 Author

| | |
|---|---|
| **Name** | Rensee Gajipara |
| **Domain** | Python Development · Data Analysis |
| **Core Skills** | Python, Pandas, NumPy, Matplotlib, Seaborn, OOP, Data Wrangling, Statistical Analysis, Data Visualization |


---

## 📝 License

This project is developed for educational purposes.

---

*Built with Python 🐍 · Powered by Pandas & Matplotlib · Data from Kaggle*
