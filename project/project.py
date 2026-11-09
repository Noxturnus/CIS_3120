import pandas as pd
import matplotlib.pyplot as plt

#Part 1: Object-oriented programming:

#create a employee class
class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept

    def compute_pay(self):
        return 0.0

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.dept}"

#create two subclasses: SalariedEmployee and HourlyEmployee
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, dept, annual_salary):
        super().__init__(emp_id, name, dept)
        self.annual_salary = annual_salary

    def compute_pay(self):
        return self.annual_salary / 12

class HourlyEmployee(Employee):
    def __init__ (self, emp_id, name, dept, hourly_rate, hours_worked):
        super().__init__(emp_id, name, dept)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def compute_pay(self):
        return self.hourly_rate * self.hours_worked


#Part 2: Pandas department KPIs:
#Read both CSV files with ‘pd.read_csv()’.
budgets = pd.read_csv('budgets.csv')
employees = pd.read_csv('employees.csv')

#Calculate each employee's pay using the objects described in Part 1.
payroll_list = []

for index, row in employees.iterrows():

    pay_type = str(row['pay_type']).strip().lower()

    if pay_type == 'salaried':
        emp = SalariedEmployee(
            row['emp_id'], row['name'], row['dept'], row['annual_salary']
        )
    elif pay_type == 'hourly':
        emp = HourlyEmployee(
            row['emp_id'], row['name'], row['dept'],
            row['hourly_rate'], row['hours_worked']
        )
    else:
        print("Unknown pay type:", row['pay_type'])
        continue
    payroll_list.append(emp.compute_pay())

employees["payroll"] = payroll_list

#Use ‘groupby()’ to calculate the total payroll for each department.
total_payroll = employees.groupby("dept")["payroll"].sum()

#Use ‘merge() to add the department budgets.
result = pd.merge(budgets, total_payroll, on="dept", how="left")

#Calculate ‘variance = budget – payroll’ for every department.
result["variance"] = result["budget"] - result["payroll"]
print(result)

#Part 3: Recursion:

def total_payroll_recursive(payroll_list):

    if len(payroll_list) == 0:
        return 0

    return payroll_list[0] + total_payroll_recursive(payroll_list[1:])
    
department_payroll_list = total_payroll.tolist()
company_total = total_payroll_recursive(department_payroll_list)
print("Total October Payroll:", f"${company_total}")


#Part 4: File output:
myFile = open("out/report.txt", "w")

myFile.write("October Payroll Report\n")
myFile.write("----------------------------\n")

myFile.write("Reporting Period: 2025-10\n")
myFile.write("Number of Employees: " + str(len(payroll_list)) + "\n")
myFile.write("Company Total Payroll: " + str(company_total) + "\n")

#For each department: payroll, budget, and variance.
myFile.write("\nDepartment:\n")

for i in range(len(result)):
    line = result["dept"].iloc[i] + ": " + str(result["payroll"].iloc[i])
    myFile.write(line + "\n")

    line = "Budget: " + str(result["budget"].iloc[i])
    myFile.write(line + "\n")

    line = "Variance: " + str(result["variance"].iloc[i])
    myFile.write(line + "\n")
myFile.close

#Part 5: Visualization and analysis:
#bar chart
plt.figure()
plt.bar(total_payroll.index, total_payroll.values)
plt.title("October 2025 Payroll by Department")
plt.xlabel("Department")
plt.ylabel("Total Payroll($)")
plt.savefig("out/payroll_chart.png")

#answer the following questions in the report.txt file:
myFile.write("-----------------------------\n")
myFile.write("Answer to the following 3 questions:\n")
highest_dept = total_payroll.idxmax()
lowest_dept = total_payroll.idxmin()
myFile.write("1. Which department has the highest payroll?\n")
myFile.write("Highest Payroll: " + highest_dept + "\n")

myFile.write("2. Which department has the lowest payroll?\n")
myFile.write("Lowest Payroll: " + lowest_dept + "\n")

myFile.write("3. Which department(s) exceeded their budget, and by how much?\n")
for i in range(len(result)):
    if result["variance"].iloc[i] < 0:
        line = result["dept"].iloc[i] + " exceeded budget by $" + str(abs(result["variance"].iloc[i]))
        myFile.write(line + "\n")

myFile.close()