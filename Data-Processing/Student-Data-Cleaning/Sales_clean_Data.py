import pandas as pd
#load file
df = pd.read_csv('Sales_Dirty.csv')

#fill the missing values in price by calculate mean
price_mean = df["Price"].mean()
df.fillna({"Price":price_mean},inplace = True)

#fill the missing duplicates with mode
quantity_mode = df["Quantity"].mode()[0]
df.fillna({"Quantity":quantity_mode},inplace = True)

# Create Total Amount column
df['Total_Amount'] = df["Quantity"] * df["Price"]

#remove the duplicate
df.drop_duplicates(inplace = True)

# Save clean file
df.to_csv("Sales_clean.csv", index=False)

print(df)


