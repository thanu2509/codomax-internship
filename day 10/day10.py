import os
import pandas as pd

# Show current working directory
print("Current Working Directory:")
print(os.getcwd())

# Show all files in the current folder
print("\nFiles in the current folder:")
print(os.listdir())

# File name
file_name = "cleaned_dataset.csv"

# Check if the file exists
if not os.path.isfile(file_name):
    print(f"\nError: '{file_name}' not found!")
    print("Place 'cleaned_dataset.csv' in the same folder as this notebook.")
else:
    # Load dataset
    df = pd.read_csv(file_name)

    print("\nDataset loaded successfully!")
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe(include="all"))

    # Display value counts for Grade if present
    if "Grade" in df.columns:
        print("\nGrade Distribution:")
        print(df["Grade"].value_counts())

    # Average study hours by Grade
    if "Grade" in df.columns and "Study_Hours" in df.columns:
        print("\nAverage Study Hours by Grade:")
        print(df.groupby("Grade")["Study_Hours"].mean())

    # Average attendance by Grade
    if "Grade" in df.columns and "Attendance" in df.columns:
        print("\nAverage Attendance by Grade:")
        print(df.groupby("Grade")["Attendance"].mean())

    # Gender-wise average exam score
    if "Gender" in df.columns and "Exam_Score" in df.columns:
        print("\nGender-wise Average Exam Score:")
        print(df.groupby("Gender")["Exam_Score"].mean())

    # Correlation for numeric columns
    print("\nCorrelation Matrix:")
    print(df.select_dtypes(include="number").corr())