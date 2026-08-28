student = {
    "aslam":3,
    "ali": 4,
    "farhan":2
}
for student_name in student:
  fail_count = student[student_name]
  if fail_count > 2:
    print(student_name ,fail_count)