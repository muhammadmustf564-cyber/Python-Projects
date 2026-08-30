import pandas as pd
import numpy as np

df = pd.read_csv('students_dirty_data.csv')

# Clean column names (IMPORTANT)
df.columns = df.columns.str.strip()

# Fill missing Age with mode
age_mode = df['Age'].mode()[0]
df['Age'] = df['Age'].fillna(age_mode)

# Fill missing Marks with mean
marks_mean = df['Marks'].mean()
df['Marks'] = df['Marks'].fillna(marks_mean)

#data of karachi students
karachi_students = df[df['City'] == 'Karachi']
print("Students of Karachi:")
print(karachi_students)

#data of lahore students
Lahore_students = df[df['City'] == 'Lahore']
print("Students of Lahore:")
print(Lahore_students)

#data of all female students
female_students = df[df['Gender'] == 'F']
print("Female_Students:")
print(female_students)

#data of all male students
male_students = df[df['Gender'] == 'M']
print("Male_Students:")
print(male_students)

#marks greater than 80
marks_greater = df[df['Marks'] > 85]
print("Marks greater than 85:")
print(marks_greater)

#sorted by marks
sorted_df = df.sort_values(by = 'Marks')
print("Sorted marks in ascending:")
print(sorted_df)

#top 5 students
top_5 = df.sort_values(by='Marks', ascending=False).head(5)
print("Top 5 Students:")
print(top_5)

#lowest 5 students
lowest_5 = df.sort_values(by = 'Marks',ascending=True).head(5)
print("Lowest 5 students:")
print(lowest_5)

#new files

#csv file
df.to_csv("student_clean_data.csv", index=False)

#Excel file
df.to_excel("student_clean_data.xlsx", index=False)

