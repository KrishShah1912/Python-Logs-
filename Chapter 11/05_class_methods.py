class Employee:
    a=15
    def show(self):
        print(f"The value of the attribute is {self.a}")

e = Employee()
e.a = 77
e.show()
# here the output will be 77 becoz it will take the value from the instance attribute only
# if you need to get output as 15 then there's the way

class x:
    a=15
    @classmethod
    def show(cls):
        print(f"The vale of the attribute is {cls.a}")

y = x()
y.a= 999
y.show()
# here output will be 15 
# only way we can do that is @classmethod and here we don't use self instead we use cls so that it get recognize and use that class-method
