class Employee:
    Salary= 1500000
    Age = 22
    Language = "English" # This is class attribute

Krish = Employee()
Krish.name= "Krish Shah" # This is object(instance) attribute
print(Krish.name , Krish.Salary ,Krish.Language)

Rohan= Employee()
Rohan.name = "Rohan Lalu " # This is object(instance) attribute
print(Rohan.name , Rohan.Salary, Rohan.Language)


# Here Name is insatance (object) attribute while  salary and language are class attribute as they directly belong to class

