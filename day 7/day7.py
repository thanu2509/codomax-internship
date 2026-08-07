import pandas as pd
import os

# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Full path to the cleaned dataset
input_file = os.path.join(current_folder, "cleaned_dataset.csv")

# Check if the file exists
if not os.path.exists(input_file):
    print("Error: 'cleaned_dataset.csv' not found!")
    print("Please make sure the file is in the same folder as day7.py")
    exit()

# Load the dataset
df = pd.read_csv(input_file)

print("Original Dataset:")
print(df)

# -----------------------------
# Basic Data Analysis
# -----------------------------

# Total
total_salary = df["Salary"].sum()

# Average
average_salary = df["Salary"].mean()

# Minimum
minimum_salary = df["Salary"].min()

# Maximum
maximum_salary = df["Salary"].max()

# Count
employee_count = df["Salary"].count()

# -----------------------------
# Display Results
# -----------------------------
print("\n----- Business Insights -----")
print(f"Total Salary      : {total_salary}")
print(f"Average Salary    : {average_salary:.2f}")
print(f"Minimum Salary    : {minimum_salary}")
print(f"Maximum Salary    : {maximum_salary}")
print(f"Total Employees   : {employee_count}")

summary = pd.DataFrame({
    "Metric": [
        "Total Salary",
        "Average Salary",
        "Minimum Salary",
        "Maximum Salary",
        "Total Employees"
    ],
    "Value": [
        total_salary,
        average_salary,
        minimum_salary,
        maximum_salary,
        employee_count
    ]
})
# Save the summary in the same folder
output_file = os.path.join(current_folder, "analysis_summary.csv")
summary.to_csv(output_file, index=False)
print("\nAnalysis summary saved successfully!")
print("Saved at:", output_file)