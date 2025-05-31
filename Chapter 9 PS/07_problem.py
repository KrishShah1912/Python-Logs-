with open("file.txt") as f:
    content1= f.read()

with open("poem.txt") as f:
    content2= f.read()

if(content1 == content2):
    print("yes files are same")

else:
    print("They are not identical")