import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class SalesDataAnalyzer:
    """
    Encapsulates all sales data analysis and visualization functionalities
    for the Superstore Sales Dataset.
    ----------
    Attributes
    data : pd.DataFrame — holds the loaded dataset
    fig  : plt.Figure — stores the last generated figure for saving
    """
    
    DATE_COL = "Order Date"
    PRODUCT_COL = "Product Name"
    CATEGORY_COL = "Category"
    SUBCAT_COL = "Sub-Category"
    REGION_COL = "Region"
    SEGMENT_COL = "Segment"
    SALES_COL = "Sales"
    PROFIT_COL = "Profit"
    DISCOUNT_COL = "Discount"
    QTY_COL = "Quantity"
    STATE_COL = "State"
    CITY_COL = "City"
    
    def __init__(self):
        self.data: pd.DataFrame = None
        self.fig: plt.figure = None
        
    def __del__(self):
        plt.close("all")
        
    #Load Data
    def loadData(self, file_path):
        """Load data from CSV and parse dates automatically."""
        try:
            self.data = pd.read_csv(file_path, encoding='latin1', sep=None, engine='python')
            
        except FileNotFoundError:
            print(f"Error: '{file_path}' not found.")
            
        else:
            for i in [self.DATE_COL, "Ship Date"]:
                if i in self.data.columns:
                    self.data[i] = pd.to_datetime(self.data[i])
                    
            if self.DATE_COL in self.data.columns:
                self.data["Year"] = self.data[self.DATE_COL].dt.year
                self.data["Month"] = self.data[self.DATE_COL].dt.month
                self.data["Month_Name"] = self.data[self.DATE_COL].dt.strftime("%b")
                
            print(f"\nDataset loaded successfully! Shape: {self.data.shape}")
            
            
    #Explore Data
    def exploreData(self):
        """Display basic information about the dataset."""
        
        if self.data is None:
            print("\nNo data loaded. Please load dataset first.")
            return
        
        print(f"\n{"=" * 10} Explore Data {"=" * 10}")
        print("1. Display first 5 rows")
        print("2. Display last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info (shape + summary)")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            print(self.data.head())
            
        elif choice == 2:
            print(self.data.tail())
        
        elif choice == 3:
            print(f"Columns: \n{list(self.data.columns)}")
            
        elif choice == 4:
            print(self.data.dtypes)
            
        elif choice == 5:
            print(f"\nShape : {self.data.shape}")
            print(f"Rows : {self.data.shape[0]}")
            print(f"Columns : {self.data.shape[1]}")
            self.data.info()
            
        else:
            print("\nInvalid Input!!")
            
            
    #clean Data
    def cleanData(self):
        """Handle missing values and perform data cleaning."""
        
        if self.data is None:
            print("\nNo data loaded. Please load dataset first.")
            return
        
        print(f"\n{"=" * 10} Handle Missing Data {"=" * 10}")
        print("1. Display rows with missing values")
        print("2. Fill numeric missing values with column mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            missing = self.data[self.data.isnull().any(axis=1)]
            print(f"\nRows with missing values: {len(missing)}")
            
            if missing.empty:
                print("\nNo missing values found in the dataset.")
                
            else:
                print(missing)
                
        elif choice == 2:
            num_col = self.data.select_dtypes(include=[np.number]).columns
            self.data[num_col] = self.data[num_col].fillna(self.data[num_col].mean())
            print("\nNumeric missing values filled with column means.")
            
        elif choice == 3:
            before = len(self.data)
            self.data.dropna(inplace=True)
            print(f"Dropped {before - len(self.data)} rows.")
            
        elif choice == 4:
            try:
                val = float(input("Enter replacement value: "))
            
            except ValueError: pass
            
            self.data.fillna(val, inplace=True)
            print(f"\nMissing values replaced with {val}.")
            
        else:
            print("\nInvalid Input!!")
            
            
    #Mathematical Operations
    def math_op(self):
        """Perform element-wise mathematical operations on numeric columns."""
        
        if self.data is None:
            print("\nNo data loaded. Please load dataset first.")
            return
        
        num_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        print(f"\nNumeric columns: {num_cols}")
        col = input("Enter column name: ").strip()
        
        arr = self.data[col].dropna().to_numpy()
        print(f"\nMathematical Operations on '{col}':")
        print(f"Sum : {np.sum(arr):,.2f}")
        print(f"Mean : {np.mean(arr):,.2f}")
        print(f"Median : {np.median(arr):,.2f}")
        print(f"Std Deviation : {np.std(arr):,.2f}")
        print(f"Variance : {np.var(arr):,.2f}")
        print(f"Min : {np.min(arr):,.2f}")
        print(f"Max : {np.max(arr):,.2f}")
        print(f"25th pct : {np.percentile(arr, 25):,.2f}")
        print(f"75th pct : {np.percentile(arr, 75):,.2f}")
        
    #Combine Data
    def com_data(self, other_dataframe):
        """Combine current DataFrame with another using concat."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        self.data = pd.concat([self.data, other_dataframe], ignore_index=True)
        print(f"\nNew shape: {self.data.shape}")
        
    #Split Data
    def split_data(self):
        """Split DataFrame by unique values of a chosen column."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        print(f"\nSuggested columns: {self.REGION_COL}, {self.CATEGORY_COL}, {self.SEGMENT_COL}, Year")
        col = input("Enter column to split on: ").strip()
        
        if col in self.data.columns:
            print("\nColumn not found.")
            return
        
        groups = {}
        for val, grp in self.data.groupby(col):
            groups[val] = grp.reset_index(drop=True)
            print(f"{val} : {len(grp):,} rows")
        return groups
    
    #Search, Sort, Filter
    def search_sort_filter(self):
        """Search, sort, and filter the Superstore dataset."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        print(f"\n{"=" * 10} DataFrame Operations {"=" * 10}")
        print("1. Search by column value")
        print("2. Sort by column")
        print("3. Filter by numeric condition")
        print("4. Filter by Region")
        print("5. Filter by Category")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            col = input("\nEnter column name to search: ").strip()
            val = input("Enter value to search for: ").strip()
            
            if col in self.data.columns:
                result = self.data[self.data[col].astype(str).str.contains(val, case=False, na=False)]
                print(f"\nFound {len(result)} matching rows.")
                print(result[[self.DATE_COL, self.PRODUCT_COL, self.REGION_COL, self.SALES_COL, self.PROFIT_COL]].head(10).to_string())
            
            else:
                print("\nColumn not found.")
                
        elif choice == 2:
            col = input("\nEnter column name to Sort : ").strip()
            asc = input("Ascending? (y/n): ").lower()
            
            if col in self.data.columns:
                print(self.data.sort_values(col, ascending=(asc == "y"))[[self.DATE_COL, self.PRODUCT_COL, self.REGION_COL, self.SALES_COL, self.PROFIT_COL]].head(10).to_string())
            
            else:
                print("\nColumn not found.")
                
        elif choice == 3:
            col  = input(f"\nNumeric column ({self.SALES_COL}, {self.PROFIT_COL}, {self.DISCOUNT_COL}): ").strip()
            cond = input("Condition (e.g. >500, <0): ").strip()
            
            try:
                result = self.data.query(f"{col} : {cond}")
                
            except Exception as e:
                print(f"Error: {e}")
                
            else:
                print(f"\nFiltered rows: {len(result):,}")
                print(result[[self.DATE_COL, self.PRODUCT_COL, self.REGION_COL, col]].head(10).to_string())
            
        elif choice == 4:
            rgns = self.data[self.REGION_COL].unique().tolist()
            print(f"\nAvailable regions: {rgns}")
            rgn = input("Enter region: ").strip()
            result = self.data[self.data[self.REGION_COL] == rgn]
            print(f"\nRegion '{rgn}': {len(result):,} rows")
            print(result[[self.DATE_COL, self.CATEGORY_COL, self.SALES_COL, self.PROFIT_COL]].head(10).to_string())
            
        elif choice == "5":
            cats = self.data[self.CATEGORY_COL].unique().tolist()
            print(f"\nAvailable categories: {cats}")
            cat = input("Enter category: ").strip()
            result = self.data[self.data[self.CATEGORY_COL] == cat]
            print(f"\nCategory '{cat}': {len(result):,} rows")
            print(result[[self.DATE_COL, self.SUBCAT_COL, self.SALES_COL, self.PROFIT_COL]].head(10).to_string())
        
        else:
            print("\nInvalid Input!!")
            
            
    #Aggregate Functions
    def agg_fun(self):
        """Apply sum, mean, count aggregations grouped by a column."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        
        print(f"\nGroup-by options: {self.REGION_COL}, {self.CATEGORY_COL}, {self.SEGMENT_COL}, {self.STATE_COL}, Year")
        grp_col = input("Enter group-by column: ").strip()
        
        if grp_col not in self.data.columns:
            print("\nColumn not found.")
            return
        
        result = self.data.groupby(grp_col)[[self.SALES_COL, self.PROFIT_COL, self.QTY_COL]].agg(["sum", "mean", "count"]).round(2)
        print(f"\nAggregated by '{grp_col}':\n")
        print(result.to_string())
        
        
    #Statistical Analysis
    def stat_analysis(self):
        """Descriptive statistics + additional NumPy stats."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        num_cols = [self.SALES_COL, self.PROFIT_COL, self.DISCOUNT_COL, self.QTY_COL]
        existing = [c for c in num_cols if c in self.data.columns]
        
        print(f"\n{"=" * 8} Descriptive Statistics {"=" * 8}")
        print(self.data[existing].describe().round(2).to_string())
        
        print(f"\n{"=" * 8} Additional Statistics {"=" * 8}")
        
        for col in existing:
            arr = self.data[col].dropna().to_numpy()
            print(f"\n{col}:")
            print(f"Variance : {np.var(arr):,.2f}")
            print(f"Std Dev : {np.std(arr):,.2f}")
            print(f"25th pct : {np.percentile(arr, 25):,.2f}")
            print(f"75th pct : {np.percentile(arr, 75):,.2f}")
            print(f"Skewness : {pd.Series(arr).skew():,.4f}")
            
            
    #Create Pivot Table
    def pivot_table(self):
        """Generate pivot tables for data summarization."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        print("\nPivot Table Options:")
        print("1. Sales & Profit by Region and Category")
        print("2. Sales by Year and Segment")
        print("3. Custom pivot table")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            pivot = pd.pivot_table(self.data, values=[self.SALES_COL, self.PROFIT_COL], index=self.REGION_COL, columns=self.CATEGORY_COL, aggfunc="sum").round(2)
            print("\nSales & Profit by Region and Category:\n")
            print(pivot.to_string())
            
        elif choice == 2:
            pivot = pd.pivot_table(self.data, values=self.SALES_COL, index="Year", columns=self.SEGMENT_COL, aggfunc="sum").round(2)
            print("\nSales by Year and Segment:\n")
            print(pivot.to_string())
            
        elif choice == 3:
            print(f"\nAvailable columns: {list(self.data.columns)}")
            idx  = input("Enter index column: ").strip()
            val  = input("Enter value column: ").strip()
            func = input("Aggregation (sum/mean/count): ").strip()
            
            try:
                pivot = pd.pivot_table(self.data, values=val, index=idx, aggfunc=func)
                print(pivot.round(2).to_string())
            
            except Exception as e:
                print(f"Error: {e}")
        
        else:
            print("\nInvalid Input!!")
            
            
    #Data Visualization
    def visualize_data(self):
        """Create plots tailored to the Superstore dataset."""
        
        if self.data is None:
            print("\nNo data loaded.")
            return
        
        print(f"\n{"=" * 10} Data Visualization {"=" * 10}")
        print("1. Bar Plot — Sales by Region")
        print("2. Line Plot — Monthly Sales Trend")
        print("3. Scatter Plot — Sales vs Profit (coloured by Discount)")
        print("4. Pie Chart — Sales Share by Segment")
        print("5. Histogram — Sales Distribution")
        print("6. Stack Plot — Yearly Sales by Category")
        print("7. Heatmap — Correlation Matrix (Seaborn)")
        print("8. Subplots — 4-in-1 Sales Dashboard")
        choice = int(input("\nEnter your choice: "))
        
        try:
            if choice == 1:
                data_grp = self.data.groupby(self.REGION_COL)[self.SALES_COL].sum()
                self.fig, ax = plt.subplots(figsize=(9, 5))
                sns.barplot(data=data_grp, x=self.REGION_COL, y=self.SALES_COL, ax=ax)
                ax.set_title("\nTotal Sales by Region", fontsize=14, fontweight="bold")
                
            elif choice == 2:
                monthly = self.data.groupby([self.data[self.DATE_COL].dt.to_period("M")])[self.SALES_COL].sum()
                monthly[self.DATE_COL] = monthly[self.DATE_COL].astype(str)
                self.fig, ax = plt.subplots(figsize=(14, 5))
                ax.plot(monthly[self.DATE_COL], monthly[self.SALES_COL], marker="o", color="#3498db", linewidth=1.5, markersize=4)
                ax.set_title("Monthly Sales Trend", fontsize=14, fontweight="bold")
                ax.set_xlabel("Month")
                ax.set_ylabel("Sales ($)")
                plt.xticks(rotation=45, ha="right", fontsize=7)
                plt.tight_layout()
                plt.show()
                print("\nLine plot displayed successfully!")
                
            elif choice == 3:
                self.fig, ax = plt.subplots(figsize=(9, 6))
                scatter = ax.scatter( self.data[self.SALES_COL], self.data[self.PROFIT_COL], c=self.data[self.DISCOUNT_COL], cmap="coolwarm", alpha=0.6, edgecolors="k", linewidths=0.3)
                plt.colorbar(scatter, ax=ax, label="Discount")
                ax.axhline(0, color="red", linewidth=1, linestyle="--")
                ax.set_title("Sales vs Profit", fontsize=14, fontweight="bold")
                ax.set_xlabel("Sales ($)")
                ax.set_ylabel("Profit ($)")
                plt.tight_layout()
                plt.show()
                print("\nScatter plot displayed successfully!")
                
            elif choice == 4:
                seg_data = self.data.groupby(self.SEGMENT_COL)[self.SALES_COL].sum()
                self.fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(seg_data.values, labels=seg_data.index, autopct="%1.1f%%", startangle=140, explode=[0.05] * len(seg_data))
                ax.set_title("Sales Share by Segment", fontsize=14, fontweight="bold")
                plt.tight_layout()
                plt.show()
                print("\nPie chart displayed successfully!")
                
            elif choice == 5:
                self.fig, ax = plt.subplots(figsize=(10, 6))
                ax.hist(self.data[self.SALES_COL].dropna(), bins=50, color="#3498db", edgecolor="white")
                ax.set_title("Sales Distribution", fontsize=14, fontweight="bold")
                ax.set_xlabel("Sales ($)")
                ax.set_ylabel("Frequency")
                plt.tight_layout()
                plt.show()
                print("\nHistogram displayed successfully!")
                
            elif choice == 6:
                pivot = self.data.pivot_table(values=self.SALES_COL, index="Year", columns=self.CATEGORY_COL, aggfunc="sum")
                self.fig, ax = plt.subplots(figsize=(10, 6))
                ax.stackplot(pivot.index, pivot.T.values, labels=pivot.columns, alpha=0.8)
                ax.legend(loc="upper left")
                ax.set_title("Yearly Sales by Category (Stacked)", fontsize=14, fontweight="bold")
                ax.set_xlabel("Year")
                ax.set_ylabel("Sales ($)")
                plt.tight_layout()
                plt.show()
                print("\nStack plot displayed successfully!")
                
            elif choice == 7:
                num_data = self.data[[self.SALES_COL, self.PROFIT_COL, self.DISCOUNT_COL, self.QTY_COL]].dropna()
                self.fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(num_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, ax=ax)
                ax.set_title("Correlation Matrix", fontsize=14, fontweight="bold")
                plt.tight_layout()
                plt.show()
                print("\nHeatmap displayed successfully!")
                
            elif choice == 8:
                self.fig, axes = plt.subplots(2, 2, figsize=(16, 10))
                self.fig.suptitle("Superstore Sales Dashboard", fontsize=16, fontweight="bold")
                
                # Top-left : Sales by Region
                reg = self.data.groupby(self.REGION_COL)[self.SALES_COL].sum()
                axes[0, 0].bar(reg.index, reg.values, color=sns.color_palette("Set2", len(reg)))
                axes[0, 0].set_title("Sales by Region")
                axes[0, 0].set_ylabel("Sales ($)")
                
                # Top-right : Profit by Category
                cat = self.data.groupby(self.CATEGORY_COL)[self.PROFIT_COL].sum()
                axes[0, 1].bar(cat.index, cat.values, color=sns.color_palette("Set3", len(cat)))
                axes[0, 1].set_title("Profit by Category")
                axes[0, 1].set_ylabel("Profit ($)")
                
                # Bottom-left : Sales vs Profit scatter
                axes[1, 0].scatter(self.data[self.SALES_COL], self.data[self.PROFIT_COL], alpha=0.4, color="red", edgecolors="k", linewidths=0.2, s=15)
                axes[1, 0].axhline(0, color="black", linewidth=0.8, linestyle="--")
                axes[1, 0].set_title("Sales vs Profit")
                axes[1, 0].set_xlabel("Sales ($)")
                axes[1, 0].set_ylabel("Profit ($)")
                
                # Bottom-right : Segment pie
                seg = self.data.groupby(self.SEGMENT_COL)[self.SALES_COL].sum()
                axes[1, 1].pie(seg.values, labels=seg.index, autopct="%1.1f%%", startangle=90)
                axes[1, 1].set_title("Sales by Segment")
                plt.tight_layout()
                plt.show()
                print("Dashboard displayed successfully!")
                
            else:
                print("\nInvalid Input!!")
                
        except Exception as e:
            print(f"\nError generating plot: {e}")
            
            
    #Save Visualization
    def save_visual(self):
        """Save the last generated figure to disk."""
        
        if self.fig is None:
            print("\nNo visualization to save. Please generate a plot first.")
            return
        
        filename = input("Enter filename to save : ")
        try:
            self.fig.savefig(filename, dpi=150, bbox_inches="tight")
            print(f"\nVisualization saved as '{filename}' successfully!")
        
        except Exception as e:
            print(f"\nError saving file: {e}")
            
            
#Menu-Driven Main Program
def menu():
    print(f"\n{"=" * 50} Data Analysis & Visualization Program {"=" * 50}")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("=" * 60)
    
def main():
    analyzer = SalesDataAnalyzer()
    
    while True:
        menu()
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            path = input("\nEnter path to CSV file: ")
            analyzer.loadData(path)
        
        elif choice == 2:
            analyzer.exploreData()
        
        elif choice == 3:
            print(f"\n{"=" * 10} Perform DataFrame Operations {"=" * 10}")
            print("1. Mathematical Operations (NumPy)")
            print("2. Search / Sort / Filter")
            print("3. Split Data by Column")
            print("4. Aggregate Functions (groupby)")
            print("5. Create Pivot Table")
            sub = int(input("\nEnter your choice: "))
            
            if   sub == 1: 
                analyzer.math_op()
                
            elif sub == 2: 
                analyzer.search_sort_filter()
                
            elif sub == 3: 
                analyzer.split_data()
                
            elif sub == 4: 
                analyzer.agg_fun()
                
            elif sub == 5: 
                analyzer.pivot_table()
                
            else: 
                print("\nInvalid Input!!")
        
        elif choice == 4:
            analyzer.cleanData()
        
        elif choice == 5:
            analyzer.stat_analysis()
        
        elif choice == 6:
            analyzer.visualize_data()
        
        elif choice == 7:
            analyzer.save_visual()
        
        elif choice == 8:
            print("\nExiting the Program. \nGood Bye!!")
            break
        
        else:
            print("\nInvalid Input!!")
            
if __name__ == "__main__":
    main()