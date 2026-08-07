# ==========================================
# Day 9 - Mini Dashboard using Matplotlib
# ==========================================

# Import Libraries
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------------------------
# Create Dataset
# ------------------------------------------
data = {
    "Subject": ["Python", "SQL", "Power BI", "Tableau", "Machine Learning"],
    "Marks": [85, 78, 90, 80, 88]
}

df = pd.DataFrame(data)

# ------------------------------------------
# Display Dataset
# ------------------------------------------
print("=" * 50)
print("         STUDENT PERFORMANCE DASHBOARD")
print("=" * 50)

print("\nDataset:")
print(df)

# ------------------------------------------
# Basic Analysis
# ------------------------------------------
average = df["Marks"].mean()
highest = df["Marks"].max()
lowest = df["Marks"].min()

highest_subject = df.loc[df["Marks"].idxmax(), "Subject"]
lowest_subject = df.loc[df["Marks"].idxmin(), "Subject"]

print("\n========== ANALYSIS ==========")
print(f"Average Marks          : {average:.2f}")
print(f"Highest Marks          : {highest}")
print(f"Lowest Marks           : {lowest}")
print(f"Best Performing Subject: {highest_subject}")
print(f"Least Performing Subject: {lowest_subject}")

# ------------------------------------------
# Create Dashboard
# ------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# ---------------- Bar Chart ----------------
axes[0].bar(df["Subject"], df["Marks"])

axes[0].set_title("Bar Chart")
axes[0].set_xlabel("Subjects")
axes[0].set_ylabel("Marks")
axes[0].tick_params(axis='x', rotation=20)

# ---------------- Line Chart ----------------
axes[1].plot(df["Subject"], df["Marks"], marker='o', linewidth=2)

axes[1].set_title("Line Chart")
axes[1].set_xlabel("Subjects")
axes[1].set_ylabel("Marks")
axes[1].grid(True)

# ---------------- Pie Chart ----------------
axes[2].pie(
    df["Marks"],
    labels=df["Subject"],
    autopct="%1.1f%%",
    startangle=90
)

axes[2].set_title("Pie Chart")

# ------------------------------------------
# Dashboard Title
# ------------------------------------------
plt.suptitle("Mini Dashboard - Student Performance Analysis", fontsize=16, fontweight="bold")

plt.tight_layout()

plt.show()

# ------------------------------------------
# Conclusion
# ------------------------------------------
print("\n========== CONCLUSION ==========")
print("✔ Dashboard Created Successfully")
print("✔ Bar Chart compares marks.")
print("✔ Line Chart shows the trend.")
print("✔ Pie Chart shows percentage distribution.")
print("✔ Basic analysis completed.")