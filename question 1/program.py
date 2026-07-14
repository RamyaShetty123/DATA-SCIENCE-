import pandas as pd

# Step 1: Create sample data
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Name": ["Asha", "Bharath", "Charan", "Deepa", "Esha", "Farhan",
             "Gita", "Hari", "Isha", "John", "Kiran", "Lakshmi"],
    "Age": [20, 21, 19, 22, 20, 23, 21, 20, 22, 19, 21, 20],
    "Marks": [85, 90, 78, 88, 92, 75, 81, 95, 89, 77, 84, 91]
}

# Step 2: Convert the data into a DataFrame
df = pd.DataFrame(data)

# Step 3: Save the DataFrame as a CSV file
df.to_csv("students.csv", index=False)

# Step 4: Load the CSV file into a DataFrame
df = pd.read_csv("students.csv")

# Step 5: Display the first 10 rows
print("First 10 Rows:")
print(df.head(10))

# Step 6: Display the number of rows and columns
print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Step 7: Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())