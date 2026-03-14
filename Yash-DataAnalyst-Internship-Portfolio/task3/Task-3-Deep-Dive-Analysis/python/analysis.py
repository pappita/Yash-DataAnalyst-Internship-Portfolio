import pandas as pd
import os

# Get current folder location
current_path = os.path.dirname(os.path.abspath(__file__))

# Build correct path to data file
file_path = os.path.join(current_path, "..", "data", "ecommerce_data.csv")

# Load dataset
data = pd.read_csv(file_path)

total_revenue = data["Revenue"].sum()
total_orders = len(data)
aov = total_revenue / total_orders

print("----- KPI RESULTS -----")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", round(aov,2))