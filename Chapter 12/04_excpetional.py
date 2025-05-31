#a = int(input("Enter the number :"))
#print(a)
# here if we enter valid number then it will print that number
# but if we entert any string then this program will throw an error
# instead of showing error we must display please enter the valid number


# so we can do this as follow:

try:
    x= int(input("Enter the number :"))
    print(x)

except Exception as e:
    print(e)

# now when we run this code it will ask user that enter the number 
# here i write krish
# it is a string
# it will print invalid literal for int()with base 10: 'krish'
# it means please enter the interger