import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/ecommerce_data.csv")

# Convert date column
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# Extract month
data["Month"] = data["Order_Date"].dt.to_period("M")

# Revenue per month
monthly_revenue = data.groupby("Month")["Revenue"].sum()

# Convert Period to string for plotting
monthly_revenue.index = monthly_revenue.index.astype(str)

# Plot
plt.figure()
plt.plot(monthly_revenue.index, monthly_revenue.values)
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()

plt.show()
