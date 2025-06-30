import pandas as pd

# File path (assuming CSV)
file_path = r"C:\Users\MAYANK\Desktop\SUMMER INTERSHIP\ASSIGNMENTS\DAY 7\data.csv"

# Load the data
df = pd.read_csv(file_path)

# Show first few rows
print("First 5 rows:")
print(df.head())

# Show summary info
print("\nDataFrame Info:")
print(df.info())

# Show missing values per column
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())
