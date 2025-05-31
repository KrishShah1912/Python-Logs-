a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

if (b==0):
    raise ZeroDivisionError("Our program is not meant for dividing a number by zero")

else:
    print(f"The dividion of {a}/{b} is {a/b}")