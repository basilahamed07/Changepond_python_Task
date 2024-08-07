
strings = "Basil Ahamed"

def while_looping_example():
    index = 0
    global strings
    while index  < len(strings):
        print(strings[index])
        index+=1        
# while_looping_example()

def _number_print():
    count = 0
    while count <=5:
        print(count)
        count+=1
# _number_print()

def _task_1():
    lists = ['hero','hercul','cycle91','bigmax',]
    index = 0
    while index < len(lists):
        print(f'{index+1}: {lists[index]}')
        index+=1
# _task_1()

def _task_2():
    student_name =('basil','ahamed','shiva','sandeep','esware')
    index = 0
    while index < len(student_name):
        print(f'{index+1}: {student_name[index]}')
        index+=1
# _task_2()


