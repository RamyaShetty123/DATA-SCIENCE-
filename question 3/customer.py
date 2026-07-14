import pandas as pd

# Customer data
data = {
    "CustomerID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Ram","Sita","Ravi","Anu","Kiran","Meena","Arjun","Priya","Rohan","Kavya"],
    "Age": [15,25,45,65,12,32,70,18,55,28],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"],
    "City": ["Bangalore","Mysore","Hubli","Mangalore","Belagavi","Bangalore","Mysore","Hubli","Dharwad","Bangalore"],
    "Income": [20000,35000,50000,40000,15000,45000,60000,25000,52000,38000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("customer.csv", index=False)

print("customer.csv created successfully!")
print(df)