def task_1():
    class Salary:
        def __init__(self,salary):
            self.base_salary =salary

        def getsalary(self):
            print("base salary: ",self.base_salary )
    
    class Allowance(Salary):
        def calculate(self):
            self.HRA = (self.base_salary/100)*20
            self.DA = (self.base_salary/100)*40
            self.TA = (self.base_salary/100)*25
        def getallocation(self):
            self.TOTAL = self.HRA+ self.DA + self.TA
            # print("Total allocation: ",self.TOTAL)
    class Dedection(Salary):
        def dedection(self):
            self.insurance = 5000
            self.pf = (self.base_salary/100)*12
            self.grati = (self.base_salary/100)*5
            self.Totaldedection = self.insurance + self.pf + self.grati
    
    class CalculateSalarySlip(Allowance,Dedection):
        
        def get_salary_slip(self):
            self.calculate()
            self.getallocation()
            self.dedection()
            print("*" *50)
            print("Base Salary: ", self.base_salary)
            print("*" * 50)
            print("total allocation: ", self.TOTAL)
            print("*" * 50)
            print("Total Dedection: ", self.Totaldedection)
            print("*" * 50)
            print("Gross Salary: ", self.base_salary + self.TOTAL)
            self.final_output = self.base_salary + self.TOTAL
            print("*" * 50)
            print("Net Salary: ", self.final_output - self.Totaldedection)
                
    #         def send_value(self):
    #             super.__init__(self.base_salary,self.final)
    print("Task 1")
    print("*" * 70)
    final = CalculateSalarySlip(int(input("Enter the base salary you got: ")))
    final.get_salary_slip()
def main():
    task_1()


if __name__ == "__main__":
    main()



