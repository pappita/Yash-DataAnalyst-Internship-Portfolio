import pandas as pd
import os

# Correct file path (works if file is in main folder)
file_path = "data/ecommerce_data.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("ERROR: File not found!")
    print("Current folder:", os.getcwd())
else:
    data = pd.read_csv(file_path)

    print("Columns in dataset:", data.columns)

    # Convert date
    data["Order_Date"] = pd.to_datetime(data["Order_Date"])

    # Extract month
    data["Month"] = data["Order_Date"].dt.to_period("M")

    # Group
    customers_per_month = data.groupby("Month")["Customer_ID"].nunique()

    print("----- Customers per Month -----")
    print(customers_per_month)