#Slide Number 17 on Lecture 2
salary=float(input("Enter the Salary:\n"))
if salary>=30000:
    years_on_job=float(input("Enter the number of years in current Job:\n"))
    if years_on_job>=2:
        print("You qualify for the loan!")
    else:
        print("You must have been in your current job for at least two years to qualify!")
else:
    print("You must earn at leats 30000 to qualify for this loan!")