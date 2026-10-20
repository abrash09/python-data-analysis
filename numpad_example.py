import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Bola", "Chidi", "Fatima", "John"],
    "Score": [75, 82, np.nan, 90, 65]
}

df = pd.DataFrame(data)

# Handle missing scores using the average
df["Score"] = df["Score"].fillna(df["Score"].mean())

# Select students who scored 70 or above
passed = df[df["Score"] >= 70]

# Calculate the average score
average = np.mean(df["Score"])

print("Updated dataset:")
print(df)

print("\nStudents scoring 70 or above:")
print(passed)

print("\nAverage score:", average)