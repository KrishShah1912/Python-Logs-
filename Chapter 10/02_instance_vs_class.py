class Employee:
    Salary= 1500000
    Age = 22
    Language = "English" # This is class attribute

Krish = Employee()
Krish.Language= "javascript"     # this is instance attribute
print( Krish.Salary ,Krish.Language)

# here output for language will be javascript becoz first it will look that is there any instance attribute or not 
# if instance attribute is present then print that only if it is not present then print class attribute value
