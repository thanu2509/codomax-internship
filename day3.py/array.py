import numpy as np

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Square:", a ** 2)
print("Square Root:", np.sqrt(a))

import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("First Element:", arr[0])
print("Last Element:", arr[-1])

print("Elements from index 1 to 4:")
print(arr[1:5])

import numpy as np

marks = np.array([85, 72, 90, 67, 88])

print("Student Marks:", marks)

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))

print("\nStudents Scoring Above Average:")
above_avg = marks[marks > np.mean(marks)]
print(above_avg)