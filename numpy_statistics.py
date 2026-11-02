import numpy as np
import pandas as pd

# Create a sample real-world style dataset
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [40, 45, 55, 60, 65, 75, 85, 90]
}

df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)

# Read CSV dataset
df = pd.read_csv("student_data.csv")

# Convert columns into NumPy arrays
hours = df["Study_Hours"].to_numpy()
marks = df["Marks"].to_numpy()

# Calculate statistics
print("Mean:", np.mean(marks))
print("Standard Deviation:", np.std(marks))
print("Correlation:", np.corrcoef(hours, marks)[0, 1])