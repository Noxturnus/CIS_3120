#Task 1: Ask the user to enter several expense categories and create list
expenses = [
    ["Rent", 1200],
    ["Food", 350],
    ["Gas", 90],
    ["Entertainment", 150],
    ["Utilities", 200]
]

#Task 2: Write the data to a file named expenses.txt
myFile = open("expenses.txt", "w")
myFile.write("Smart Expense Tracker Report\n")
myFile.write("----------------------------\n")

for expense in expenses:
    myFile.write(expense[0] + ": " + str(expense[1]) + "\n")

myFile.close()


#Task 3: Calculate Expense Statistics
categories = ["Rent", "Food", "Gas", "Entertainment", "Utilities"]
amounts = [1200, 350, 90, 150, 200]

def average(numbers):
    return sum(numbers) / len(numbers)

total = sum(amounts)
highest = max(amounts)
lowest = min(amounts)
avg = average(amounts)
aboveAverage = sum(amount > avg for amount in amounts)

print("Total Expenses:", total)
print("Highest Expense:", categories[amounts.index(highest)], "-", highest)
print("Lowest Expense:", categories[amounts.index(lowest)], "-", lowest)
print("Average Expense:", avg)
print("Categories Above Average:", aboveAverage)


#Task 4: Append Results to File
myFile = open("expenses.txt", "a")
myFile.write("\n----------------------------\n")
myFile.write("Total Expenses: " + str(total) + "\n")
myFile.write("Highest Expense: " + categories[amounts.index(highest)] + " - " + str(highest) + "\n")
myFile.write("Lowest Expense: " + categories[amounts.index(lowest)] + " - " + str(lowest) + "\n")
myFile.write("Average Expense: " + str(avg) + "\n")
myFile.write("Categories Above Average: " + str(aboveAverage) + "\n")
myFile.close()


#Task 5: Sort Expenses from Highest to Lowest
sortedAmounts = sorted(amounts, reverse=True)

myFile = open("expenses.txt", "a")
myFile.write("\nSorted Expenses (High to Low):\n")

for amount in sortedAmounts:
    line = categories[amounts.index(amount)] + ": " + str(amount)
    print(line)
    myFile.write(line + "\n")

myFile.write("----------------------------\n")
myFile.close()


#Task 6: Read Final Report
myFile = open("expenses.txt", "r")
print("\nFinal Expense Report:")
print(myFile.read())
myFile.close()
