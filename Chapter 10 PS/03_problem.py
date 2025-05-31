class Demo:
    
    a = 4

o = Demo()

print(o.a) # print the class attribute becoz instance attribute is not present here

o.a = 0 # instance attribute created here

print(o.a) # instance is available now so instance will be printed

print (Demo.a) # prints class attribute 