# a = int(input("Enter the number :"))
# b = int(input("Enter the number :"))
# c = int(input("Enter the number :"))

# average = (a+b+c)/3
# print(average)

#  for 50 users we have to enter and then print so it will increase line in my data code

# Instead we can use function

# function definition 
def avg():
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    c = int(input("Enter the number :"))

    average = (a+b+c)/3
    print(average)

# now we have given command that if someone want to run avg then do this 
# but if we run this prog till now then it won't provide any output

avg() # this are function call
avg()
avg()
avg()
avg()

# if want to get 5 times average then do avg() 5 times ..... so it will give you answer

# the function can be called anywhere and we can call it anytime according to our convinient
