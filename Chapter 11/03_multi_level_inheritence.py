class Employee:
    a=1

class Coder(Employee):
    b=2

class x(Coder):
    c=3

o = Employee()
print(o.a)  # it will print 1
#print(o.b)  # it will throw error as there is no b attribute in Employee class

o=Coder()
print(o.a, o.b)
# here both will give output such as 1 and 1 2