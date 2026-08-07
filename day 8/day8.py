import matplotlib.pyplot as plt

# Sample Data
subjects = ["Python", "SQL", "Power BI", "Tableau", "Machine Learning"]
marks = [85, 78, 90, 80, 88]

# -------------------------------
# Bar Chart
# -------------------------------
plt.figure(figsize=(6,4))
plt.bar(subjects, marks)
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# -------------------------------
# Line Chart
# -------------------------------
plt.figure(figsize=(6,4))
plt.plot(subjects, marks, marker='o')
plt.title("Marks Trend")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# -------------------------------
# Pie Chart
# -------------------------------
plt.figure(figsize=(6,6))
plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Marks Distribution")
plt.show()