n =int(input("Enter the number of students: "))
student_marks ={}
for _ in range(n):
    data = input("Enter students name and their marks:").split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name]= marks
query_name = input()
marks =student_marks[query_name]
average = sum(marks)/len(marks)
print("Average of query name: ",f"{average:.2f}")

