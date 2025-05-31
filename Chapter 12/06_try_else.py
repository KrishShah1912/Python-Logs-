try:
    x= int(input("Enter the number :"))
    print(x)

except Exception as e:
    print(e)

else:
    print("I am inside else")


#if try will be succesful then it will enter else 
# if try will be wrong then it won't enter else