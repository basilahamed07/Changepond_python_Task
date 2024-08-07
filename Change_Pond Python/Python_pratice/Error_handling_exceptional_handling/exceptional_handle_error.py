# is will handling the error while during program exicuction
# in this exceptional handling we have two types 
#    -> try
#    -> except
# in this we have three catgories they are :
    # -> specific except handling
    # -> general except handling
    # -> default except handling

# example

# nums = [1,2,3,4,5,6,7,8,9,9]

# try:
#     for trash in range(1,20):
#         print(trash,"-",nums[trash])
# except:
#     print("Index out of range")


def specific():
    try:
        num1 = int(input("Enter the num1: "))
        num2 = int(input("Enter the num2: "))
        lists = [1,2,3]
        final = num1//num2 
        # lists[len(lists)] = 2
        assert num1%2 == 0
    except ZeroDivisionError:
        return ("num2 can't be a zero")
    except ValueError:
        return ("You only enter the numeric values")
    except AssertionError:
        return("enter value is not matching with testcase")
    except IndexError:
        print("kindly use the insert 0r append method to add the list items")
    else:
        print(num1)
    finally:
        print("Program over")
# print(specific())
def datetimees():
    import datetime
    try:
        today = datetime.date.today()
        years = today.year
        yob = int(input("Enter the year of birth: "))
        age = years - yob
    except ValueError:
        return ("You only enter the numeric values")
    if(age < 18):
        raise Exception(f"the age should be grater then 18 and your age is {age}")
   
    else:
        return (age)
print(datetimees())