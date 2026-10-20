import pandas as pd
import statsmodels.api as sm

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Score": [50, 55, 65, 70, 78, 85]
}

df = pd.DataFrame(data)

# Define the independent variable
X = df["Study_Hours"]

# Add the intercept
X = sm.add_constant(X)

# Define the dependent variable
y = df["Score"]

# Fit the regression model
model = sm.OLS(y, X).fit()

# Display the statistical results
print(model.summary())