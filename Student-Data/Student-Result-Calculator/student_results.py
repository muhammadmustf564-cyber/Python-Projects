
student_marks = {}

with open("students_marks.txt", "r") as file:

    for line in file:

        data = line.split()

        name = data[0]
        marks = list(map(float, data[1:]))

        student_marks[name] = marks


with open("results.txt", "w") as file:

    num_of_subjects = len(next(iter(student_marks.values())))

    # Header
    file.write(f"{'Student Name':<15}")

    for i in range(num_of_subjects):
        file.write(f"{'Subject ' + str(i + 1):<12}")

    file.write(f"{'Total Marks':<15}")
    file.write(f"{'Obtained Marks':<18}")
    file.write(f"{'Average':<12}")
    file.write(f"{'Percentage':<12}\n")


    # Results
    for name, marks in student_marks.items():

        obtained_marks = sum(marks)

        total_marks = len(marks) * 50

        average = obtained_marks / len(marks)

        percentage = (obtained_marks / total_marks) * 100


        file.write(f"{name:<15}")

        for mark in marks:
            file.write(f"{mark:<12.1f}")

        file.write(f"{total_marks:<15}")
        file.write(f"{obtained_marks:<18.1f}")
        file.write(f"{average:<12.2f}")
        file.write(f"{percentage:<12.2f}%\n")

