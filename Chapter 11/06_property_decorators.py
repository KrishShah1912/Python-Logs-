class Employee:
    a=15

    @classmethod
    def show(cls):
        print(f"The value of the attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 77
e.name = "Krish Shah"
print(e.fname, e.lname)
e.show()