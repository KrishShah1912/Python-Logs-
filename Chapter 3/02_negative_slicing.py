name ="krish"
print(name[0:3])
print(name[-4:-1])
# here don't use negative slicing instead use positive one 
# roughly convert negative slice to equivalent positive and run program
# so for -4 to -1 do  1 to 4
print(name[1:4])
print(name[:4]) # here at empty space in start it means zero '0', which is quivalent to [0:4]
print(name[1:]) # is same as [1:5]


xyz = "abcdefghijklmnopqrstuvwxyz"
print (xyz[1:9]) # output will be 'bcdefghi'
print (xyz[1:9:4]) # output will be 'bf' becoz b will be printed 1st then skip 4 so you will reach f then again skip 4 till end

print (len(name)) # lenght of string 
print (name.endswith("sh")) # ouput will be true
print(name.endswith("k")) # output will be false)
print (name.startswith("kris")) # output will be true
print (name.capitalize()) # here output will be in capital way like krish conver to Krish, only 1st character only get capatilized 

# see python handbook there are many other functions which are quite basic and easy to use