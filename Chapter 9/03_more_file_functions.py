#f= open("file.txt", "r")
#lines = f.readlines()
#print(lines, type(lines))
#f.close()

f= open("file.txt")

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

f.close()

# from line 6 to 20 it will print all lines in one single line