import pandas as pd

# Load the student performance data from a CSV file
data = pd.read_csv('students_performance.csv')
print("First rows of data:")
print(data.head())

# Compute the average math score
math_avg = data['Math Score'].mean()
print(f"Average math score: {math_avg:.2f}")

# Calculate average score for each student
data["Average Score"] = data[["Math Score", "Science Score", "English Score"]].mean(axis=1)

print("\nStudent-wise Average Scores:")
print(data[["Name", "Average Score"]])

import matplotlib.pyplot as plt

# Bar chart of student average scores
plt.bar(data["Name"], data["Average Score"])
plt.xlabel("Student Name")
plt.ylabel("Average Score")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Pass / Fail classification
data["Result"] = data["Average Score"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nPass/Fail Status:")
print(data[["Name", "Result"]])



