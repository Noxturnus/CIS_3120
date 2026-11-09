#Tals 1: Write Grades to file
import pandas as pd
import matplotlib.pyplot as plt

grades = [80, 90, 50, 60, 70, 67, 99, 100, 85, 88]

myFile = open("grades.txt", "w")

for grade in grades:
    myFile.write(str(grade) + "\n")

myFile.close()


#Task 2 Read Grades from the File

myFile = open("grades.txt", "r")
gradeLine = [int(line) for line in myFile.readlines()]
myFile.close()
print("Grade:", grades)

#Task 3: Create an average return
def average(numbers):
    return sum(numbers) / len(numbers)
print("-----------------")
print("The average is", round(average(gradeLine),2))

#Task 4:
df = pd.DataFrame({'Student':range(1, len(grades)+1), 'Grade':grades})
stats = df["Grade"].describe().round(2)
print('--------------------------')
print('Grade Statistics', stats)

#Task 5:
myFile = open('grades.txt', 'a')
myFile.write('\nSum: ' + str(df['Grade'].sum()))
myFile.write('\nMax: ' + str(df['Grade'].max()))
myFile.write('\nAverage: ' + str(df['Grade'].mean()))
myFile.close()

myFile=open("report.txt",'w')
myFile.write(stats.to_string())
myFile.close()

#Task 6: create graphs
df.plot(x = 'Student', y = 'Grade', kind = 'bar', legend = False, title = "Student Grades")
plt.axhline(df['Grade'].mean(), color = 'red', linestyle = '--', label = "Class Average")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.tight_layout()
plt.savefig("grades_bar_chart.png")
plt.close()

df.plot(y = 'Grade', kind = 'hist', bins = 5, legend = False, title = "Grades Distribution")
plt.axvline(df['Grade'].mean(), color = 'red', linestyle = '--', label = "Class Average")
plt.xlabel("Grade")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("grades_histogram.png")
plt.close()

