# country = ['india','south korea', 'iran','japan','trukey','iraq']
# #slow process
# print(country[0]) # india
# print(country[1]) # south korea
# print(country[2]) # iran
# print(country[3]) # japan

# # by using the for loop we can archive the code reducing
# print('by using the for loop by using the range function')
# for trash in range(len(country)):
#     print(country[trash])
    
    
# print('by using the for loop by using the collection')
# index  = 1
# for trash in country:
#     print(f"{index}:{trash.title()}" )
#     index+=1
    
# print("by using the while loopinhg")
# index = 0
# index_ref = 1
# while index < len(country):
#     print((f"{index_ref}:{country[index].title()}" ))
#     index+=1
#     index_ref+=1
author_name =('j k rowling',"rachel aaron",'hans aanrud','verna aadana')
def task_1():
    global author_name
    index = 1
    for trash in range(len(author_name)):
        print(f'{index} : {author_name[trash].title()}')
        index+=1
# task_1()

def range_function():
    print("by using the sing value")
    for trash in range(2):
        print(trash)
    print("by using the two values")
    for trash in range(2,2):
        print(trash)
    print("by using the three values")
    for trash in range(2,10,2):
        print(trash)
    print("by using the arathmatic or type casting in inside the range function")
    for trash in range(2,11//2,2):
        print(trash)
# range_function()

def using_the_range_function_print_collection():
    global author_name
    for trash in range(len(author_name)):
        print(trash+1,author_name[trash])
# using_the_range_function_print_collection()

def Task_2():
    time_update = "it's 4:15pm"
    for trash in time_update:
        print(trash)
    print("By using the range function")
    for trash in range(len(time_update)):
        print(time_update[trash])
Task_2()


