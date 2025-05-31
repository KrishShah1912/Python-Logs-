class Employee:
    Salary= 1500000
    Age = 22
    Language = "English" # This is class attribute

    def __init__(self, name, Salary , Age , Language):   # Dunder Method which is automatically called 
        self.name = name
        self.Salary= Salary
        self.Age = Age
        self.Language = Language
        print("I am creating a object")
    

    def getInfo(self):
        print(f"The salary is {self.Salary}. . The language preference is {self.Language}")


    @staticmethod
    def greet():
        print("Good Morning")


Krish = Employee("Krish", 15000000, 24, "Python")
print( Krish.Salary ,Krish.Language, Krish.Language, Krish.Age)

