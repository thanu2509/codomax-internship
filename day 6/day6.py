import pandas as pd
import os
# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the CSV file
file_path = os.path.join(current_folder, "cleaned_dataset.csv")

df = pd.read_csv(file_path)
print("Original Dataset:")
print(df)

filtered_rows = df[df["Age"] > 25]

print("\nFiltered Rows (Age > 25):")
print(filtered_rows)
# -----------------------------
# 2. Select Columns
# -----------------------------
selected_columns = df[["Name", "Age", "Salary"]]

print("\nSelected Columns:")
print(selected_columns)
# -----------------------------
# 3. Sort Dataset
# -----------------------------
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted Dataset (Salary - Highest to Lowest):")
print(sorted_df)
# ----------------------------
# 4. Save the Filtered Dataset
# -----------------------------
output_path = os.path.join(current_folder, "filtered_dataset.csv")
sorted_df.to_csv(output_path, index=False)

print("\nFiltered dataset saved successfully!")
print("Location:", output_path)