student ={
    "aslam" : [{"maths":50,"science":60,"urdu":49,"english":70}],
    "ali": [{"maths":70,"science":70,"urdu":47,"english":46}],
    "sameer": [{"maths":49,"science":59,"urdu":60,"english":38}],
    "fawad" :[{"maths":34,"science":48,"urdu":90,"english":70}],
}
for student_name in student:
 x = student[student_name][0]
 fail_count = 0
 
 for marks in x.values():
   if marks < 50:
     fail_count +=1

 print(student_name , "failed" , fail_count , "subjects")