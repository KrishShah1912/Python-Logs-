class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name}, and his age is {self.age}")

#class programmer:
  # company = "ITC INFOTECH"
   #def show(self):
    #   print(f"The name of the employee is {self.name}, and his age is {self.age}")

   #def show(self):
    #   print (f"the name is {self.language}")
# here problem will be that i have to copy paste the part of employee to programmer
# it's also easy task but when there will be 50 task and suddenly i have to change some content then at all 50 places i have to change 
# which is not efficient so we have to use inheritence concept here
class programmer(Employee):
    company = "TCS"
    def show(self):
        print(f"The language for this candidate is {self.langauage}")
# here if there are 100 items and suddenly need to chage some details then only have to change it in Employee part only
# And by changing it, it will ultimately apply to all other areas
# so better to use inheritance concept for convininec
a=Employee()
b= programmer()
print(a.company, b.company)