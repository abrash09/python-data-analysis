import pandas as pd

data = {
    "Name": ["Ali", "Bola", "Chidi", "Fatima", "John"],
    "Age": [20, 21, 19, 22, 20],
    "Score": [75, 82, 68, 90, 85]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())