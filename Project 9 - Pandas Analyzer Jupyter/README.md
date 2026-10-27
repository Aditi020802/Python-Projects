# 📊 Project 9 – Pandas Analyzer & Data Visualization

<div align="center">

### 🐼 A Python Data Analysis and Visualization Application

**Load • Explore • Clean • Analyze • Visualize • Export**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Implemented-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Implemented-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Visualization](https://img.shields.io/badge/Data%20Visualization-Matplotlib%20%7C%20Seaborn-2ea44f?style=for-the-badge)

</div>

---

## ✨ Overview

**Pandas Analyzer & Data Visualization** is a menu-driven Python project that helps users load, explore, clean, transform, analyze, visualize, and export tabular data from CSV files.

The project uses **Pandas** for data manipulation, **NumPy** for numerical operations, **Matplotlib** and **Seaborn** for charts, and a `SalesDataAnalyzer` class to organize its features.

The included Jupyter Notebook provides a convenient environment to run the project and review its outputs. The sample dataset is provided in `sales_data.csv`.

## 🎯 Project Objectives

- Read and work with CSV datasets using Pandas.
- Explore rows, columns, data types, and dataset dimensions.
- Identify and handle missing values and duplicate rows.
- Perform mathematical operations on numeric columns.
- Combine and split datasets.
- Search, sort, and filter data.
- Calculate aggregates and descriptive statistics.
- Create pivot tables and perform NumPy array operations.
- Visualize data with Matplotlib and Seaborn.
- Save charts and export processed data.

## 🚀 Features

| Menu | Feature | Description |
|:---:|---|---|
| 1 | Load Dataset | Loads a CSV file into a DataFrame |
| 2 | Explore Data | Displays first/last rows, columns, data types, information, and shape |
| 3 | Clean Missing Data | Displays missing rows, fills missing values, drops missing rows, and removes duplicates |
| 4 | Mathematical Operations | Adds or multiplies values and calculates profit margin or Sales + Profit |
| 5 | Combine DataFrames | Concatenates rows or merges datasets using a common column |
| 6 | Split DataFrame | Filters rows by a selected column value and saves them to a CSV |
| 7 | Search, Sort and Filter | Searches values and filters by numeric threshold, category, or date range |
| 8 | Aggregate Functions | Calculates sum, mean, count, grouped totals, and transformed group averages |
| 9 | Statistical Analysis | Displays descriptive statistics, standard deviation, variance, quantiles, and correlations |
| 10 | Create Pivot Table | Creates and optionally exports a pivot table |
| 11 | NumPy Array Operations | Displays numeric data as an array and performs indexing, slicing, addition, and multiplication |
| 12 | Data Visualization | Creates charts using Matplotlib and Seaborn |
| 13 | Save Visualization | Saves the most recently created chart as an image |
| 14 | Export Analysis Data | Exports the current DataFrame to CSV |
| 15 | Exit | Ends the application |

## 🖥️ Main Menu

```text
=======================================================
       PANDAS ANALYZER & DATA VISUALIZATION
=======================================================
1.  Load Dataset
2.  Explore Data
3.  Clean Missing Data
4.  Mathematical Operations
5.  Combine DataFrames
6.  Split DataFrame
7.  Search, Sort and Filter
8.  Aggregate Functions
9.  Statistical Analysis
10. Create Pivot Table
11. NumPy Array Operations
12. Data Visualization
13. Save Visualization
14. Export Analysis Data
15. Exit
=======================================================
Enter your choice:
```

## 🧱 Main Class and Responsibilities

| Class / Method | Description |
|---|---|
| `SalesDataAnalyzer` | Main class that manages dataset analysis |
| `__init__()` | Initializes the DataFrame, file path, and plot reference |
| `load_data()` | Reads a CSV file and converts relevant columns to suitable data types |
| `explore_data()` | Displays dataset structure and information |
| `clean_data()` | Handles missing values and duplicate rows |
| `mathematical_operations()` | Performs numeric calculations and creates derived columns |
| `combine_data()` | Concatenates or merges DataFrames |
| `split_data()` | Saves a filtered subset to a new CSV file |
| `search_sort_filter()` | Searches, sorts, and filters records |
| `aggregate_functions()` | Calculates aggregates and grouped summaries |
| `statistical_analysis()` | Computes descriptive statistics and correlation |
| `create_pivot_table()` | Creates and optionally saves a pivot table |
| `numpy_operations()` | Converts numeric columns to a NumPy array for array operations |
| `visualize_data()` | Generates charts using Matplotlib and Seaborn |
| `save_visualization()` | Saves the most recently created plot |
| `export_data()` | Exports the current dataset to CSV |
| `main()` | Runs the menu loop and calls the selected feature |

## 📈 Data Visualization

The project supports nine visualization options:

1. **Bar Chart** — total sales by product.
2. **Line Chart** — sales trend over time.
3. **Scatter Plot** — relationship between sales and profit.
4. **Pie Chart** — each product's share of sales.
5. **Histogram** — distribution of a selected numeric column.
6. **Stack Plot / Stacked Bar Chart** — sales by product and region.
7. **Subplots** — multiple charts in one figure.
8. **Seaborn Heatmap** — correlation between numeric columns.
9. **Seaborn Box Plot** — distribution and spread of a numeric column.

After creating a chart, use menu option **13** to save the most recent visualization as a `.png`, `.jpg`, or `.jpeg` file.

## 🧠 Python Libraries and Concepts Used

| Library / Concept | Usage |
|---|---|
| `pandas` | Reading CSV files, cleaning data, grouping, merging, filtering, and pivot tables |
| `numpy` | Numerical calculations, array conversion, and correlation-related operations |
| `matplotlib.pyplot` | Creating and saving charts |
| `seaborn` | Statistical charts, histograms, box plots, scatter plots, and heatmaps |
| `DataFrame` | Stores and manipulates tabular data |
| `read_csv()` | Loads data from CSV files |
| `to_csv()` | Exports data and results |
| `isnull()` / `fillna()` | Detects and fills missing values |
| `dropna()` / `drop_duplicates()` | Removes missing rows and duplicate records |
| `groupby()` | Groups data for aggregation |
| `merge()` / `concat()` | Combines DataFrames |
| `pivot_table()` | Summarizes data in a pivot table |
| `describe()` | Generates descriptive statistics |
| `select_dtypes()` | Selects columns by data type |
| `try-except` | Handles selected file and input errors |
| `class` and `self` | Organizes project logic using OOP |
| Menu loop and conditionals | Supports interactive menu selection |

## 📂 Project Structure

```text
Project 9 - Pandas Analyzer Jupyter/
│
├── Project_9_Pandas_Analyzer.ipynb
├── README.md
├── sales_data.csv
│
└── Output/
    ├── output-1.png
    ├── output-2.png
    ├── output-3.png
    ├── output-4.png
    ├── output-5.png
    ├── output-6.png
    ├── output-7.png
    ├── output-8.png
    ├── output-9.png
    ├── output-10.png
    ├── output-11.png
    ├── output-12.png
    └── output-13.png
```

The `Output` folder contains the screenshots included with this project. `sales_data.csv` is the sample dataset, and `Project_9_Pandas_Analyzer.ipynb` contains the notebook code and execution cells.

## 📸 Output Screenshots

The following images are included in the `Output` folder. Click an image in GitHub to view it at full size.

<div align="center">

### 🖥️ Output 1

<img src="Output/output-1.png" alt="Pandas Analyzer Output 1" width="90%">

### 🖥️ Output 2

<img src="Output/output-2.png" alt="Pandas Analyzer Output 2" width="90%">

### 🖥️ Output 3

<img src="Output/output-3.png" alt="Pandas Analyzer Output 3" width="90%">

### 🖥️ Output 4

<img src="Output/output-4.png" alt="Pandas Analyzer Output 4" width="90%">

### 🖥️ Output 5

<img src="Output/output-5.png" alt="Pandas Analyzer Output 5" width="90%">

### 🖥️ Output 6

<img src="Output/output-6.png" alt="Pandas Analyzer Output 6" width="90%">

### 🖥️ Output 7

<img src="Output/output-7.png" alt="Pandas Analyzer Output 7" width="90%">

### 🖥️ Output 8

<img src="Output/output-8.png" alt="Pandas Analyzer Output 8" width="90%">

### 🖥️ Output 9

<img src="Output/output-9.png" alt="Pandas Analyzer Output 9" width="90%">

### 🖥️ Output 10

<img src="Output/output-10.png" alt="Pandas Analyzer Output 10" width="90%">

### 🖥️ Output 11

<img src="Output/output-11.png" alt="Pandas Analyzer Output 11" width="90%">

### 🖥️ Output 12

<img src="Output/output-12.png" alt="Pandas Analyzer Output 12" width="90%">

### 🖥️ Output 13

<img src="Output/output-13.png" alt="Pandas Analyzer Output 13" width="90%">

</div>

## 🎬 Project Demonstration

A project demonstration video can be added to the project folder to show the complete workflow: loading a dataset, exploring and cleaning data, performing analysis, generating visualizations, and exporting results.

If you add a video, save it in the project folder and update this section with its exact filename and path.

## ⚙️ How to Run the Project

### Option 1: Run in Jupyter Notebook

1. Extract the ZIP file.
2. Open the project folder in Jupyter Notebook, JupyterLab, or Google Colab.
3. Open `Project_9_Pandas_Analyzer.ipynb`.
4. Make sure `sales_data.csv` is available in the notebook's working directory.
5. Run the notebook cells from top to bottom.

### Option 2: Install Required Libraries

Run the following command in a terminal or notebook cell:

```bash
python -m pip install pandas numpy matplotlib seaborn jupyter
```

### Option 3: Run as a Python Script

The supplied project is a Jupyter Notebook. To run it as a standalone Python script, export or save the code into a `.py` file first, then run that file from the same directory as `sales_data.csv`.

```bash
python sales_analyzer.py
```

Replace `sales_analyzer.py` with the actual filename if you use a different name.

## 📦 Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook, JupyterLab, or Google Colab for notebook execution
- Sample dataset: `sales_data.csv`

## 🎓 Learning Outcomes

By completing this project, the learner practices:

- Loading and inspecting real-world-style CSV data.
- Understanding rows, columns, data types, and DataFrame shape.
- Handling missing values and duplicate records.
- Applying mathematical operations to columns.
- Combining and splitting datasets.
- Searching, sorting, and filtering records.
- Performing grouping, aggregation, and pivot-table analysis.
- Calculating descriptive statistics and correlation.
- Using NumPy arrays alongside Pandas.
- Creating charts with Matplotlib and Seaborn.
- Saving visualizations and exporting processed data.
- Structuring a menu-driven analysis project with a Python class.

## 🚧 Possible Future Improvements

- Add automated tests for each menu option.
- Add more robust validation for file paths and user inputs.
- Include a `requirements.txt` file.
- Add a data summary dashboard.
- Allow users to select multiple columns for analysis.
- Add more chart types and customizable chart settings.
- Generate an automatic PDF or HTML analysis report.
- Add a GUI or web-based dashboard.

## 📊 Project Snapshot

| Category | Details |
|---|---|
| Project | Pandas Analyzer & Data Visualization |
| Project Number | 9 |
| Language | Python 3.x |
| Main Class | `SalesDataAnalyzer` |
| Main Libraries | Pandas, NumPy, Matplotlib, Seaborn |
| Data Format | CSV |
| Notebook | `Project_9_Pandas_Analyzer.ipynb` |
| Dataset | `sales_data.csv` |
| Visualization Options | 9 |
| Output Screenshots | 13 included |
| Application Type | Menu-driven data analysis project |

## 👤 Developer

<div align="center">

### **Aditi Modhvadiya**

**Python • Pandas • NumPy • Data Analysis • Data Visualization**

Built for learning and practice.

</div>

---

<div align="center">

### ⭐ Project 9 – Pandas Analyzer

**Load → Clean → Analyze → Visualize → Export**

[⬆ Back to Top](#-project-9--pandas-analyzer--data-visualization)

</div>
