import pandas as pd
import matplotlib.pyplot as plt


pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
#Task 1 Load the Dataset

df = pd.read_csv('sales_data.csv')
print(df.head(5))
print()

#Task 2 Create New Columns
df["Revenue"] = df["Quantity"] * df["Price"]
df["Date"] = pd.to_datetime(df["Date"])
print(df)
print()

#Task 3 Descriptive statistics
df.describe()
print()
average_revenue = df.groupby("Product")["Revenue"].mean()
print("Product with the highest average revenue:",average_revenue.idxmax())
print()

#Task 4 filter and sorting
print("Transaction with Revenue more than $250:")
print(df[df["Revenue"] > 250])
print()
print("Top 3 transactions by Revenue:")
print(df.sort_values("Revenue", ascending=False).head(3))
print()
#Task 5 Grouping
total_revenue = df.groupby("Product")["Revenue"].sum()
print("Total Revenue Per Product:",total_revenue)
print()

total_revenue_region = df.groupby("Region")["Revenue"].sum()
print("Total Revenue Per Region:",total_revenue_region)
print()

#Task 6 Visualization

#Bar chart
plt.figure()
plt.bar(total_revenue.index, total_revenue.values)
plt.title("Total Revenue Per Product")
plt.xlabel("Product")
plt.ylabel("Revenue($)")
plt.show()

#pie chart
plt.figure()
plt.pie(total_revenue_region, labels=total_revenue_region.index, autopct='%1.1f%%')
plt.title("Share of Revenue by Region")
plt.show()


#line chart
plt.figure()
daily_revenue = df.groupby("Date")["Revenue"].sum()

plt.plot(daily_revenue.index, daily_revenue.values, marker='o')
plt.title("Daily Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue($)")
plt.xticks(rotation=45)
plt.show()
