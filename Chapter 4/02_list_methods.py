x= ["krish", "rahul", "kohli", 107,34.56, 'False',"Shankar"]
print(x)

x.append ("KL") # append means it get append at last place
print (x) # here we apply change to list and list get changed


y = [89,87,25,63,4,36,71,2,34,25]
y.sort() # here all numbers will be sorted according to ascending order
print(y) 

yy = [3,56,76,235,64,256,34673,22,1,4,5]
yy.reverse() # here complete list will be reversed
print(yy)

yyy = [3,23,453,456,755,1,23,87,65,98]
yyy.insert (2, 123456789) # here formate is first index and then number 
print (yyy)
# append will insert at last place only but insert is used to insert any number in between and anywhere you want

yyy.pop(4) # index 4 will be poped out
print (yyy)
print (yyy.pop(5)) # here it will print the index 5 number individual
