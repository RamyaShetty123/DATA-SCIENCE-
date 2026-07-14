# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("students.csv")

# Display the dataset
print("Student Dataset:")
print(df)

# Select numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64'])

# -----------------------------
# Histogram of Numerical Features
# -----------------------------
plt.figure(figsize=(8, 6))
numerical_columns.hist(figsize=(10, 8), bins=10, edgecolor='black')
plt.suptitle("Histogram of Numerical Features")
plt.tight_layout()

# Save Histogram
plt.savefig("histogram.png")
plt.show()

# -----------------------------
# Box Plot to Detect Outliers
# -----------------------------
plt.figure(figsize=(8, 6))
sns.boxplot(data=numerical_columns)
plt.title("Box Plot of Numerical Features")

# Save Box Plot
plt.savefig("boxplot.png")
plt.show()

# -----------------------------
# Explanation
# -----------------------------
print("\nExplanation:")
print("1. Histogram shows the distribution of numerical features.")
print("2. Box Plot helps detect outliers.")
print("3. Points outside the whiskers indicate outliers.")