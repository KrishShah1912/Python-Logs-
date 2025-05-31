with open("xyz.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present in the content")
else:
    print("python is not present in the content")

