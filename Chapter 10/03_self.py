class Employee:
    Salary= 1500000
    Age = 22
    Language = "English" # This is class attribute


    def getInfo(self):
        print(f"The salary is {self.Salary}. . The language preference is {self.Language}")


    @staticmethod
    def greet():
        print("Good Morning")


Krish = Employee()
Krish.Language= "javascript"     # this is instance attribute
print( Krish.Salary ,Krish.Language)

Krish.greet()
# It will not required you to add self becoz we have already added @staticmethod initially 

Krish.getInfo()
# this will get converted into Employee.getinfo(Krish)
# so need to add something in getinfo(-----)
