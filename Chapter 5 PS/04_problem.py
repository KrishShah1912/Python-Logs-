s = set()
s.add(18)
s.add("18")
s.add(18.0)
print(len(s))

# here in python 1==1.0 will return true that's why 18 and 18.0 is treated as one number only
