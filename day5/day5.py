import pandas as pd
import os


current_folder = os.path.dirname(os.path.abspath(__file__))

# CSV file path
csv_path = os.path.join(current_folder, "day5.csv")

# Read dataset
df = pd.read_csv(csv_path)

print("========== ORIGINAL DATA ==========")
print(df)

# -----------------------------
# Handle Missing Values
# -----------------------------

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing Department
df["Department"] = df["Department"].fillna("Unknown")

# Fill missing Joining_Date
df["Joining_Date"] = df["Joining_Date"].fillna("Not Available")

# -----------------------------
# Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Correct Data Types
# -----------------------------
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)

df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce"
)

# -----------------------------
# Display Results
# -----------------------------
print("\n========== CLEANED DATA ==========")
print(df)

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
output_path = os.path.join(current_folder, "cleaned_dataset.csv")
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Location:", output_path)