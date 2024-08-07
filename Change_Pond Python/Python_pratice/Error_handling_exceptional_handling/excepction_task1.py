import os
def task_1():
    try:
        assert (os.path.exists(r"D:\Software-Training-Basil_ahamed\Python Pratice\Change_Pond Python\Python_pratice\Variables\variables.py"))
        
        # file not found error
        def filenotfound():
            var1  = open(r"D:\Software-Training-Basil_ahamed\Python Pratice\Change_Pond Python\Python_pratice\Variables\variables.p","r")
        # filenotfound()
        var2 = open(r"D:\Software-Training-Basil_ahamed\Python Pratice\Change_Pond Python\Python_pratice\Functions\FUNCTION\Function.txt","a")
        varread = open(r"D:\Software-Training-Basil_ahamed\Python Pratice\Change_Pond Python\Python_pratice\Functions\FUNCTION\Function.txt","r")
        #Attribute error
        def attribute_error():
            new_data = var2.open("Hello how are you")
        #calling attribute error
        # attribute_error()
        
        #name error #hello
        def nameerror():
            new_data = var2.write(hello)
        # nameerror()
        
        def typeserror(varread):
            varread = int(varread)
            print(varread)
        # typeserror(varread)
        def modulenotfounderror():
            import checkss
        modulenotfounderror()
    except AssertionError:
        print("file not exist")
    except FileNotFoundError:
        print("Enter the correct file name")
    except AttributeError:
        print("This was attribute error")
    except NameError:
        print("check the variable or enter the valid variable")
    except TypeError:
        print("cant you check the type of the ")
    except ModuleNotFoundError:
        print("Check the method name")
    finally:
        print("Program run successfully")
task_1()