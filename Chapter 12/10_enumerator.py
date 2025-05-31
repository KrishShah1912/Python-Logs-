l = [ 1, 45, 63, 18, 4,23, 456, 773,2]

#index = 0
#for item in l:
#    print(f"The item number at index {index} is {item}")
#    index = index + 1

# this can be simplified using enumerator function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")