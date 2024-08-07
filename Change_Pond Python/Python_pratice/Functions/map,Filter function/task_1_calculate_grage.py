def calculate_input():
    marks = {}
    for trash in range(0,1):
        marks["Python"] = int(input("Enter the Python Mark:"))
        marks["Cloud Computing"] = int(input("Enter the Cloud Computing Mark:"))
        marks["Cyber Security"] = int(input("Enter the Cyber Security Mark:"))
        marks["Network_security"] = int(input("Enter the Network_security Mark:"))
        marks["Angular"] = int(input("Enter the Angular Mark:"))
    return marks

def calculate_grads(final,result):
    # result = {
    #     400:"Your Grade: O :)",
    #     300:'Your Grade: A',
    #     200:"Your Grade: B",
    #     100:'Your Grade: F'}
    final = sum(final.values())
    if final >= 400:
        return result[400]
    elif final <=399 and final >=300:
        return result[300]
    elif final <=299 and final >=200:
        return result[200]
    elif final < 200:
        return result[100]
    
    
def by_using_filter(values):
    result = {
        400:"Your Grade: O :)",
        300:'Your Grade: A',
        200:"Your Grade: B",
        100:'Your Grade: F'}
    if values >= 80:
        return result[400]
    elif values <= 79 and values >= 60:
        return result[300]
    elif values <= 59 and values >= 40:
        return result[200]
    elif values <40:
        return result[100]
def main():
    result = {
        400:"Your Grade: O :)",
        300:'Your Grade: A',
        200:"Your Grade: B",
        100:'Your Grade: F'}
    
    marks = calculate_input()
    print("By using the filter function")
    final_values = marks.values()
    print(final_values)
    print("____By Using Filter function_____")
    final = list(filter(by_using_filter,final_values))
    print(final)
    # print()
    # print("________Result_________")
    # print(calculate_grads(marks,result))
if __name__ == "__main__":
    main()