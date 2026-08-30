import pandas as pd

# Load dirty sales data
df = pd.read_csv("sales_dirty_data.csv")

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Fill missing Price values with the mean price
price_mean = df["Price"].mean()
df["Price"] = df["Price"].fillna(price_mean)

# Fill missing Quantity values with the mode
quantity_mode = df["Quantity"].mode()[0]
df["Quantity"] = df["Quantity"].fillna(quantity_mode)

# Create Total Amount column
df["Total_Amount"] = df["Quantity"] * df["Price"]

# Save cleaned data as CSV
df.to_csv("sales_clean_data.csv", index=False)

# Save cleaned data as Excel
df.to_excel("sales_clean_data.xlsx", index=False)

# Display cleaned data
print("\nCleaned Sales Data:")
print(df)

print("\nData cleaning completed successfully!")
print("Created files:")
print("- Sales_clean_data.csv")
print("- Sales_clean_data.xlsx")
