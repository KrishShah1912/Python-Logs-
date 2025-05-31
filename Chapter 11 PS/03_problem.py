class Employee:
    salary = 234
    increment = 25

    @property
    def salaryinc(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryinc.setter
    def salaryinc(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()

e.salaryinc = 290  # This should update increment without errors.
print(e.increment)  # It should now print the updated value of increment.
