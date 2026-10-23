import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:
    REQUIRED_COLUMNS = ["Date", "Product", "Category", "Price", "Quantity Sold", "Total Sales"]

    def __init__(self):
        self.data = pd.DataFrame()
        self.filtered_data = None

    def load_data(self, file_path):
        if not isinstance(file_path, str) or not file_path.strip():
            print("Error: Please enter a valid CSV file path.")
            return False
        if not os.path.isfile(file_path):
            print("Error: File not found. Check the path and try again.")
            return False
        if not file_path.lower().endswith(".csv"):
            print("Error: The input file must have a .csv extension.")
            return False
        try:
            self.data = pd.read_csv(file_path)
        except (pd.errors.ParserError, UnicodeDecodeError, OSError) as error:
            print(f"Error reading CSV: {error}")
            return False
        missing_columns = [column for column in self.REQUIRED_COLUMNS if column not in self.data.columns]
        if missing_columns:
            print("Error: Required column(s) missing:", ", ".join(missing_columns))
            self.data = pd.DataFrame()
            return False
        print(f"Loaded {len(self.data)} rows successfully.")
        return True

    def validate_data(self):
        if self.data.empty:
            print("No dataset loaded. Choose option 1 first.")
            return
        print("\nDATA VALIDATION REPORT")
        print("-" * 45)
        for column in self.REQUIRED_COLUMNS:
            missing_count = int(self.data[column].isna().sum())
            blank_count = int(self.data[column].astype(str).str.strip().eq("").sum())
            if missing_count or blank_count:
                print(f"{column}: {missing_count + blank_count} missing/blank value(s)")
            else:
                print(f"{column}: no missing values")
        print(f"Duplicate rows: {int(self.data.duplicated().sum())}")
        print("Checking numeric fields...")
        for column in ["Price", "Quantity Sold", "Total Sales"]:
            numeric_values = pd.to_numeric(self.data[column], errors="coerce")
            invalid_count = int(numeric_values.isna().sum())
            if invalid_count:
                print(f"{column}: {invalid_count} non-numeric or missing value(s)")
            if column in ["Price", "Quantity Sold"]:
                negative_count = int((numeric_values < 0).sum())
                if negative_count:
                    print(f"{column}: {negative_count} negative value(s)")

    def clean_data(self):
        if self.data.empty:
            print("No dataset loaded. Choose option 1 first.")
            return
        before = len(self.data)
        df = self.data.copy()
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        for column in ["Price", "Quantity Sold", "Total Sales"]:
            df[column] = pd.to_numeric(df[column], errors="coerce")
        df["Product"] = df["Product"].replace(r"^\s*$", np.nan, regex=True)
        df["Category"] = df["Category"].replace(r"^\s*$", np.nan, regex=True)
        df = df.dropna(subset=["Date", "Product", "Category", "Price", "Quantity Sold"])
        df = df[(df["Price"] >= 0) & (df["Quantity Sold"] >= 0)]
        # Recalculate Total Sales so blank or inconsistent totals are corrected.
        df["Total Sales"] = (df["Price"] * df["Quantity Sold"]).round(2)
        df = df.drop_duplicates().reset_index(drop=True)
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        self.data = df
        self.filtered_data = None
        print(f"Cleaning complete: {before} rows -> {len(self.data)} rows.")
        print(f"Removed {before - len(self.data)} row(s) due to invalid/missing data or duplicates.")

    def calculate_metrics(self):
        if self.data.empty:
            print("No clean data available. Load and clean the dataset first.")
            return None
        df = self.data
        sales_array = df["Total Sales"].to_numpy(dtype=float)
        total_sales = float(np.sum(sales_array))
        average_sale = float(np.mean(sales_array))
        product_units = df.groupby("Product")["Quantity Sold"].sum().sort_values(ascending=False)
        popular_product = product_units.index[0] if not product_units.empty else "N/A"
        daily_sales = df.assign(Date=pd.to_datetime(df["Date"])).groupby("Date")["Total Sales"].sum().sort_index()
        if len(daily_sales) >= 2 and daily_sales.iloc[0] != 0:
            growth_rate = float(((daily_sales.iloc[-1] - daily_sales.iloc[0]) / daily_sales.iloc[0]) * 100)
        else:
            growth_rate = 0.0
        return {"total_sales": total_sales, "average_sale": average_sale,
                "popular_product": popular_product, "popular_product_units": int(product_units.iloc[0]) if len(product_units) else 0,
                "growth_rate": growth_rate, "transactions": len(df)}

    def display_summary(self):
        metrics = self.calculate_metrics()
        if metrics is None:
            return
        print("\nRETAIL SALES SUMMARY")
        print("=" * 45)
        print(f"Number of records : {metrics['transactions']}")
        print(f"Total sales       : ${metrics['total_sales']:,.2f}")
        print(f"Average sale      : ${metrics['average_sale']:,.2f}")
        print(f"Most popular item : {metrics['popular_product']} ({metrics['popular_product_units']} units)")
        print(f"First-to-last daily sales change: {metrics['growth_rate']:.2f}%")
        print("\nSales by category:")
        print(self.data.groupby("Category")["Total Sales"].sum().sort_values(ascending=False).round(2).to_string())

    def filter_data(self, condition):
        if self.data.empty:
            print("No dataset loaded. Choose option 1 first.")
            return pd.DataFrame()
        df = self.data.copy()
        print("\nFilter options: 1. Category  2. Product  3. Date range")
        choice = input("Choose filter type: ").strip()
        if choice == "1":
            value = input("Enter category: ").strip()
            result = df[df["Category"].str.casefold() == value.casefold()]
        elif choice == "2":
            value = input("Enter product name: ").strip()
            result = df[df["Product"].str.casefold() == value.casefold()]
        elif choice == "3":
            start_text = input("Start date (YYYY-MM-DD): ").strip()
            end_text = input("End date (YYYY-MM-DD): ").strip()
            start_date = pd.to_datetime(start_text, errors="coerce")
            end_date = pd.to_datetime(end_text, errors="coerce")
            if pd.isna(start_date) or pd.isna(end_date) or start_date > end_date:
                print("Invalid date range.")
                return pd.DataFrame()
            dates = pd.to_datetime(df["Date"])
            result = df[(dates >= start_date) & (dates <= end_date)]
        else:
            print("Invalid filter option.")
            return pd.DataFrame()
        self.filtered_data = result.copy()
        print(f"Found {len(result)} matching record(s).")
        if result.empty:
            print("No matching records.")
        else:
            print(result.to_string(index=False))
        return result

    def aggregate_data(self):
        if self.data.empty:
            print("No dataset loaded. Choose option 1 first.")
            return
        print("\nSALES BY PRODUCT")
        print(self.data.groupby("Product").agg(total_sales=("Total Sales", "sum"), units_sold=("Quantity Sold", "sum")).sort_values("total_sales", ascending=False).round(2).to_string())
        print("\nSALES BY CATEGORY")
        print(self.data.groupby("Category")["Total Sales"].sum().sort_values(ascending=False).round(2).to_string())
        print("\nSALES BY DATE")
        print(self.data.assign(Date=pd.to_datetime(self.data["Date"])).groupby("Date")["Total Sales"].sum().sort_index().round(2).to_string())

    def save_clean_data(self, output_path="retail_sales_cleaned.csv"):
        """Save cleaned data to a new CSV file."""
        if self.data.empty:
            print("No data to save. Load and clean the dataset first.")
            return
        self.data.to_csv(output_path, index=False)
        print(f"Cleaned dataset saved to: {output_path}")

    def plot_category_sales(self):
        if self.data.empty:
            print("No dataset loaded.")
            return
        summary = self.data.groupby("Category")["Total Sales"].sum().sort_values(ascending=False)
        plt.figure(figsize=(9, 5))
        sns.barplot(x=summary.index, y=summary.values)
        plt.title("Total Sales by Product Category")
        plt.xlabel("Product Category")
        plt.ylabel("Total Sales ($)")
        plt.xticks(rotation=25, ha="right")
        plt.tight_layout()
        plt.show()

    def plot_sales_trend(self):
        if self.data.empty:
            print("No dataset loaded.")
            return
        daily = self.data.assign(Date=pd.to_datetime(self.data["Date"])).groupby("Date")["Total Sales"].sum().sort_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=daily.index, y=daily.values, marker="o")
        plt.title("Retail Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales ($)")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self):
        if self.data.empty:
            print("No dataset loaded.")
            return
        numeric = self.data[["Price", "Quantity Sold", "Total Sales"]].corr(numeric_only=True)
        plt.figure(figsize=(7, 5))
        sns.heatmap(numeric, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
        plt.title("Correlation: Price, Quantity Sold, and Total Sales")
        plt.tight_layout()
        plt.show()


def show_menu():
    print("RETAIL SALES DATA ANALYZER")
    print("1. Load CSV dataset")
    print("2. Validate dataset")
    print("3. Clean data")
    print("4. Display summary metrics")
    print("5. Filter data")
    print("6. Aggregate sales reports")
    print("7. Bar chart: sales by category")
    print("8. Line graph: sales trend")
    print("9. Heatmap: numerical correlation")
    print("10. Save cleaned dataset")
    print("0. Exit")


def main():
    analyzer = RetailAnalyzer()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            file_path = input("Enter CSV path (e.g. retail_sales.csv): ").strip()
            analyzer.load_data(file_path)
        elif choice == "2":
            analyzer.validate_data()
        elif choice == "3":
            analyzer.clean_data()
        elif choice == "4":
            analyzer.display_summary()
        elif choice == "5":
            analyzer.filter_data(None)
        elif choice == "6":
            analyzer.aggregate_data()
        elif choice == "7":
            analyzer.plot_category_sales()
        elif choice == "8":
            analyzer.plot_sales_trend()
        elif choice == "9":
            analyzer.plot_correlation_heatmap()
        elif choice == "10":
            output_path = input("Output CSV path [retail_sales_cleaned.csv]: ").strip() or "retail_sales_cleaned.csv"
            analyzer.save_clean_data(output_path)
        elif choice == "0":
            print("Thank you for using Retail Sales Data Analyzer.")
            break
        else:
            print("Invalid choice. Enter a number from 0 to 10.")


if __name__ == "__main__":
    main()
