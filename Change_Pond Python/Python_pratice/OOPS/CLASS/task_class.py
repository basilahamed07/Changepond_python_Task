def task_1(values):
    class Prodect:
        _product_id = 0
        
        def  add_function(self,pname,pprice,pdesc):
            self.pname = pname
            self.pprice = pprice
            self.pdesc = pdesc
            Prodect._product_id += 1 
            self.__id = self._product_id
            print("Prodect add sucessfully")
        def get_product_names(self):
            print("*" * 50,self.__id,"*" * 50)
            print(f"product name: {self.pname}")
            print(f"product price: {self.pprice}")
            print(f"product description: {self.pdesc}")
            print(f"product id: {self.__id}")
    
    lists = []
    for trash in range(1,values+1):
        lists+=[f"product_{trash}"]
    for trash in lists:
        trash = Prodect()
        trash.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
        trash.get_product_names()

def main():
    task_1(int(input("How many Product you like to add: ")))

if __name__ == "__main__":
    main()