# here rem is function created by me 
# it will take input from l as list and word
def rem(l, word):
    # we will run for loop to find our string in list
    for item in l:
        # after finding our string we will remove it from list l
        l.remove(word)
        # we will return the remaining part of string as it is
        return l
    # so return l
   

# here we created a list named with l
l = ["krish", "an", "rohan"] 
# here we will print the remaining list 
# but there a catch that we will remover string name "an"
print(rem(l, "an"))

# output will be ['krish', 'rohan']


# if we write this code inside rem()
# then it will remove word string "an" from all the strings
# like output will be ['krish', 'roh']
# here an string will be removed and an from rohan will be also removed

# n=[]
    #for item in l:
     #   if not(item==word):
      #      n.append(item.strip(word))
    #return n