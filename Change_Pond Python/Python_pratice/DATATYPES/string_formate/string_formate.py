# string  formating by using the #f word

student_name = input("Enter the student name here: ")
student_id =int(input("Enter the student_id:"))


#types of methods
#upper()
#title()
#lower()
print(F' Student Name: {student_name.upper()} \n student_id :{student_id}')
print(F' Student Name: {student_name.title()} \n student_id :{student_id}')
print(F' Student Name: {student_name.lower()} \n student_id :{student_id}')

#title case


# another way to perform the formate 

print("Student name: {} \nstudent id:{}".format(student_name,student_id))
#error data
print("Student id: {} \nstudent id:{}".format(student_id,student_name))


