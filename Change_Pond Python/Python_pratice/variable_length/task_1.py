def task(*args):
    result = ""
    index=1
    for trash in args[0]:
        print(f"{index}:{trash}")
        index+=1
    value = int(input("Enter the dish you like: "))
    main_dish = args[0][value-1]
  
    topings = []
    while True:
        index=1
        for trash in args[1]:
            print(f"{index}:{trash}")
            index+=1
        
        topings_value = int(input("Enter the topings: "))
        if topings_value <= 3:
            topings += [args[1][topings_value-1]]
        else:
            break
    final = {main_dish:topings}
    return final,main_dish
def main():
    dish,main_dish = (task(["sanwitch","burgur","pizza"],
                           ["spicy","cheesy","peporony","Exit"]))
    print(f" your food was = {main_dish}, \nand your addon = {dish[main_dish]}")
if __name__ == "__main__":
    main()
    
