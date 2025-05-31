class programmer:
    company = "Microsoft"

    def __init__(self, name , age , salary, pincode):
        self.name = name
        self.age = age
        self.salary = salary
        self.pincode = pincode

p = programmer("Krish", 22, 1400000, 380061)
q = programmer("Rohan", 25, 1100000, 380034)
r = programmer("Rahul", 29, 100000, 380090)
s = programmer("Saunik", 39, 1100000, 380181)
t = programmer("Aditya", 20, 1000000, 3800001)
y = programmer("Dhruv", 44, 400000, 380091)
o = programmer("Hardi", 19, 700000, 380088)
d = programmer("Yash", 21, 190000, 380033)
print(p.name, p.age, p.salary, p.pincode, p.company)
print(q.name, q.age, q.salary, q.pincode, q.company)
print(r.name, r.age, r.salary, r.pincode, r.company)
print(s.name, s.age, s.salary, s.pincode, s.company)
print(t.name, t.age, t.salary, t.pincode, t.company)
print(y.name, y.age, y.salary, y.pincode, y.company)
print(o.name, o.age,o.salary, o.pincode, o.company)
print(d.name, d.age, d.salary, d.pincode, d.company)
