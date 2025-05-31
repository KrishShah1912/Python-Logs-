myList = [ 1 , 3 , 4  ,  5 , 7]

#squaredList = []
#for item in myList:
#    squaredList.append(item*item)
#print(squaredList)

# here we don't need to write this whole stroy 
# directly we can do with the help of list comprehension

squaredList = [i*i for i in myList]
print(squaredList)