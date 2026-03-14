import pandas as pd
from datetime import datetime

# Load dataset
df = pd.read_csv("data/raw_sales_data.csv")

print("Initial Shape:", df.shape)

# Data Profiling
print(df.info())
print(df.describe())
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# Handle Missing Values
df['amount'].fillna(df['amount'].median(), inplace=True)
df['city'].fillna("Unknown", inplace=True)

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Dates
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce', dayfirst=True)
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')

# Remove Outliers
df = df[df['amount'] < 100000]

# Feature Engineering - Age
current_year = datetime.now().year
df['age'] = current_year - df['date_of_birth'].dt.year

# Save Clean Data
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("Final Shape:", df.shape)
print("Data Cleaning Completed Successfully.")
