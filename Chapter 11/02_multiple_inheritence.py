class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the company is {self.company}")

class coder:
    language = "python"
    def printlangauge(self):
        print(f"out of all the langauges here it is your langauge {self.language}")

class programmer(Employee, coder):
    company = "TCS"
    def showx(self):
        print(f"The company for this candidate is {self.company}")

a=Employee()
b= programmer()


b.show()
b.printlangauge()
b.showx()
