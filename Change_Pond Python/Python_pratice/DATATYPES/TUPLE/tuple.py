def tuple_datatype():
    tuple_datatype = (1,2,3,4,5,6,6,8,9,0,"basil")
    print(tuple_datatype)
    student_id = (123,124,125,126) #homogenius
    ice_cream = ("vanilla","choco-chips",'blueberry') #homogenius
    mixed_type = (123,"hello",False,56.78)
    print(len(mixed_type))
    print(ice_cream[2])
    print(mixed_type[-2])
    print(mixed_type[1:3])
    #it will considerr as trhe stirng
    ice_cream = ("vennila")
    print(ice_cream)
    #it will consider as tuple datatypes
    ice_cream = ("vennila" ,)
    print(ice_cream)
# tuple_datatype()

def tuple_methods():
        ice_cream = ("vanilla","choco-chips",'blueberry',"vanilla") #homogenius
        #count it return the repited values
        print(ice_cream.count("vanilla"))

        #index method
        print(ice_cream.index("vanilla"))
    
tuple_methods()


