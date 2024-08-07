# task 1

def task_2_python(var1,var2):
    print()
    print("Python task 2")
    print("before change the variable name..")
    print()
    print(var1)
    print(var2)
    print()
    print("after change the variable name..")
    var1= 'change the value var1'
    var2= 'changed value var2'
    print()
    print(var1)
    print(var2)

    
def task_1_python(var):
    print("Python Task 1")
    print()
    return f' you enter : {var}'
print(task_1_python(var=input("Enter the value here:")))
task_2_python(var1=input("Enter the first value:"),var2=input("Enter the second value:"))   


