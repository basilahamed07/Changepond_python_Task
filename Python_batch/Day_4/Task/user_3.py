# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.



# Hi!

# [Your Name] here from [Brand Name]. Super excited you’re with us!

# Need help or got questions? I’m just a text away.



# Hello, my name is (name). I am a (year in school) studying (major) at Western Michigan University. Goal: I am looking for (internship/full-time position) at (employer name). Interest/passion: I am interested in (interests related to the company/industry).
class Users:
    def __init__(self):
        self.create_instance()
    def create_instance(self):
        self.first_name = input("ENter the First Name:")
        self.last_name = input("Enter the last name:")
        self.age = int(input("Enter the age:"))
        self.status = input("Enter the marrage status:")
        self.company = input("Enter the company name:")
        self.domain = input("ENter the Domain:")
    def describe_user(self):
       return f"Hello, my name is {self.first_name} {self.last_name}. I am a Working in {self.company} in the position of  {self.domain}. and i am {self.age} Old, i am {self.status} "
    def greet_user(self):
        return f"""
Hi {self.first_name} {self.last_name}, here from Basil Technology!

Congrats! You’ve just unlocked special member perks 🎉

Stay tuned for personalized deals and insider info.""" 


def main():
    #user 1
    user1 = Users()
    print(user1.describe_user())
    print(user1.greet_user())
    #user 2
    user2 = Users()
    print(user2.describe_user())
    print(user2.greet_user())
    #user 3
    user3 = Users()
    print(user3.describe_user())
    print(user3.greet_user())
    #user 4
    user4 = Users()
    print(user4.describe_user())
    print(user4.greet_user())

if __name__ == "__main__":
    main()