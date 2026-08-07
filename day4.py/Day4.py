import pandas as pd
import os
# Display the current working directory
print("Current Working Directory:", os.getcwd())
# Display all files in the current directory
print("\nFiles in the current directory:")
print(os.listdir())

file_path = "sample_dataset.csv"

# Load the CSV dataset
df = pd.read_csv(file_path)

# Display the first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display the column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display the shape of the dataset
print("\nDataset Shape:")
print(df.shape)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())