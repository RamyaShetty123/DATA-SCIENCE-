import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the CSV you already created
df = pd.read_csv("customer.csv")

# i. Create Age Group feature
def age_group(age):
    if age <= 12:
        return "Child"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)

# ii. One-hot encode categorical features
categorical_cols = ["Gender", "City", "AgeGroup"]
df_encoded = pd.get_dummies(df, columns=categorical_cols)

# iii. Min-Max scale numerical features
numerical_cols = ["Age", "Income"]
scaler = MinMaxScaler()
df_encoded[numerical_cols] = scaler.fit_transform(df_encoded[numerical_cols])

# iv. Save transformed data
df_encoded.to_csv("customer_transformed.csv", index=False)

print("Transformed data saved as customer_transformed.csv")
print(df_encoded)