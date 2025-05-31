f = open("file.txt", "r") # here r is for read and default mode is read only so it will work without r if you want to just read
data = f.read()
print(data)
f.close()
