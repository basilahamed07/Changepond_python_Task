import math

def task_6(nums):
    result =[]
    for trash in range(1,nums):
        result += [math.sqrt(trash)]
    return result
def main():
    print(task_6(int(input("Enter the range of the number:"))))

if __name__ == "__main__":
    main()
    