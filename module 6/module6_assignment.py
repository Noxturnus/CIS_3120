#Task 1 Load the Dataset
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('retail_sales.csv')

#Task 2 Initial Inspection
print("Task 2: Initial Inspection")
print()

print(df.head(5))
print()

print(df.dtypes)
print()

print(df.isnull().sum())
print()

print(df.duplicated().sum())
print()

df = df.drop_duplicates()

#Task 3 Create New Columns
print("Task 3: Create New Columns")
print()

df["Net_Revenue"] = df["Revenue"] * (1 - df["Discount"])
df["Return_Rate"] = df["Returns"] / df["Units_Sold"]
df["Date"] = pd.to_datetime(df["Date"])

#Task 4 Descriptive Statistics
print("Task 4: Descriptive Statistics")
print()

print(df[["Units_Sold", "Revenue", "Net_Revenue"]].describe())
print()

average_revenue = df.groupby("Units_Sold")[["Revenue", "Net_Revenue"]].mean()
print(average_revenue)
print()

print("Product with the highest average revenue:",average_revenue["Net_Revenue"].idxmax())
print()

#Task 5 Filtering and Sorting
print("Task 5: Filtering and Sorting")
print()

print("Transaction with Net_Revenue greater than 2000:")
print(df[df["Net_Revenue"] > 2000])
print()

print("Top 5 transactions by Net_Revenue:")
print(df.sort_values("Net_Revenue", ascending=False).head(5))
print()

#Task 6 Grouping and Aggregation
print("Task 6: Grouping and Aggregation")
print()

product_category = df.groupby("Product_Category")["Units_Sold"].sum()
print("Total Units Sold:")
print(product_category)
print()

product_category = df.groupby("Product_Category")["Net_Revenue"].sum()
print("Total Net Revenue:")
print(product_category)
print()

product_category = df.groupby("Product_Category")["Return_Rate"].mean()
print("Average Return Rate:")
print(product_category)
print()

#group by Store and find: Total Net Revenue per Store
store_revenue = df.groupby("Store")["Net_Revenue"].sum()
print("Total Net Revenue per Store:")
print(store_revenue)
print()

#Task 7 Visualization
print("Task 7: Visualization")
print()

#Bar chart
plt.figure()
plt.bar(product_category.index, product_category.values)
plt.title("Total Net Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue($)")
plt.show()

#pie chart
plt.figure()
plt.pie(store_revenue, labels=store_revenue.index, autopct='%1.1f%%')
plt.title("Share of Net Revenue by Store")
plt.show()


#line chart
plt.figure()
daily_Over_Net_Revenue = df.groupby("Date")["Net_Revenue"].sum()

plt.plot(daily_Over_Net_Revenue.index, daily_Over_Net_Revenue.values, marker='o')
plt.title("Daily Total Net Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue($)")
plt.xticks(rotation=45)
plt.show()
