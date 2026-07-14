# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the student dataset
df = pd.read_csv("student.csv")

# Display the first 5 rows
print("First 5 Rows of the Dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Select only numerical columns
numerical_features = df.select_dtypes(include=['int64', 'float64'])

# -------------------------------
# Histogram of Numerical Features
# -------------------------------
numerical_features.hist(figsize=(12, 8), bins=10, edgecolor='black')

plt.suptitle("Histogram of Numerical Features")
plt.tight_layout()
plt.show()

# -------------------------------
# Box Plot of Numerical Features
# -------------------------------
plt.figure(figsize=(10, 6))

sns.boxplot(data=numerical_features)

plt.title("Box Plot of Numerical Features")
plt.xlabel("Features")
plt.ylabel("Values")
plt.xticks(rotation=45)

plt.show()