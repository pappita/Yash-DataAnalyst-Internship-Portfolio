import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "Customer_ID": np.random.randint(1000, 2000, n),
    "Order_ID": np.arange(1, n+1),
    "Order_Date": pd.date_range(start="2023-01-01", periods=n, freq="D"),
    "Revenue": np.random.randint(500, 5000, n)
})

# Create data folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

data.to_csv("data/ecommerce_data.csv", index=False)

print("Dataset created successfully!")
print(data.head())