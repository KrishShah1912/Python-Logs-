# c/5 = f-32/9 formula of celcius to fehrenite
# c = 5*(f-32)/9

def ftoc(f):

    c = 5*(f-32)/9
    return c

f = int(input("Enter the temperature in fehrenite : "))
xy = ftoc(f) 
# here for readaptivity i have used xy variable and stored the value in it
# better to used this type of content for better looking of the program
print(f"The corresponding temperature in degree celcius is :{round(xy, 2)}")  

# here we have used round becoz it's showing so much after decimal like 2.4444444 so beeter to round off it 
# round(value, upto whatt decimal like here we used 2)

if(ftoc(f)> 25):
    print("It's to hot!")

else:
    print("It's not to hot")
