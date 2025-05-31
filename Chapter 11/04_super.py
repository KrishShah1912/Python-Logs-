class Employee:
    def __init__(self):
        print("constructor of Employee")
    a=1

class Coder(Employee):
      def __init__(self):
        print("constructor of Coder")
      b=2

class x(Coder):
      def __init__(self):
        super().__init__()
        print("constructor of x")
      c=3

# here when we attach super keyword then when we will run x then automatically his parent will also run so x parent is coder
# so coder will also run

#o = Employee()
#print(o.a)  # it will print 1
#print(o.b)  # it will throw error as there is no b attribute in Employee class

#o=Coder()
#print(o.a, o.b)
# here both will give output such as 1 and 1 2

o=x()
print(o.a,o.b,o.c)