try:
    a= int(input("Enter the a number :"))
    b= int(input("Enter the b number :"))
    print(a/b)

except ZeroDivisionError as x:
    print("Infinity")


