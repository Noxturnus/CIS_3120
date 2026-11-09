import pandas as pd
import matplotlib.pyplot as plt


#Task 1 Create a DataFrame
df = {"Student_Name": ["Ace", "Boomer", "Charlotte", "Dva", "Eva"],
        "Hours_Studied": [5, 9, 10, 6, 7],
        "Exam_Score": [67, 85, 99, 76, 80],}

df = pd.DataFrame(df)
print("Task 1: Full DataFrame:")
print(df)
print()

#Task 2 Basic exploration
print("Task 2a: First 3 Rows:")
print(df.head(3))
print()
print("Task 2b: Summary Statistics:")
print(df.describe())
print()

#Task 3 Filtering and sorting
print("Task 3: Students who studied more than 8 hours:")
print(df[df["Hours_Studied"] > 8])
print()

#Task 4 Data manipulation
print("Task 4: Add the New column Performance")

def performance(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    else: 
        return "Needs Improvement"
df["Performance_level"] = df["Exam_Score"].apply(performance)
print(df)
print()

#Task 5 Summary Statistics
print("Task 5: Summary Statistics")
print("Average Exam Score:", round(df["Exam_Score"].mean(), 2))
print()
#average_score = df["Exam_Score"].mean()
#print("Average Exam Score:", average_score)

print("The highest number of study hours:",df["Hours_Studied"].max())
print()
#highest_study_hours = df["Hours_Studied"].max()
#print("Highest Hours Studied:", highest_study_hours)

#Task 6 Visualization
print("Bar chart showing")
plt.figure(figsize=(8, 5))
plt.bar(df["Student_Name"],df["Hours_Studied"], color='skyblue')
plt.title("Hours Studied by Students")
plt.xlabel("Student Name")
plt.ylabel("Hours Studied")
plt.show()

print("scatter plot showing")
plt.figure(figsize=(8, 5))
plt.scatter(df["Hours_Studied"],df["Exam_Score"], color='skyblue', s=80)
for i in range(len(df)):
    plt.annotate(df["Student_Name"][i], 
                 (df["Hours_Studied"][i], df["Exam_Score"][i]), 
                 textcoords="offset points", xytext=(5,5))

plt.title("Hours Studied VS Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)
plt.show()
print()