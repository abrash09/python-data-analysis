import numpy as np
from scipy import stats

scores = np.array([75, 82, 68, 90, 85])

# Descriptive statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores, ddof=1)

print("Mean:", mean_score)
print("Median:", median_score)
print("Sample standard deviation:", round(std_score, 2))

# One-sample t-test against a population mean of 75
result = stats.ttest_1samp(scores, popmean=75)

print("T-statistic:", round(result.statistic, 3))
print("P-value:", round(result.pvalue, 4))