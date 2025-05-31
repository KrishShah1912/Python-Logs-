def inches_to_cms(n):
    return n * 2.54

n = float(input("Enter the value in inches :"))
# here we use float becoz inches can not completely in integer
# so beeter to use float so that int can also covered

print(f"The corresponding value in cms is {inches_to_cms(n)}")