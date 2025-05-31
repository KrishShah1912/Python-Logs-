marks = int(input("Enter your marks :"))

if(marks > 100):
    print("Enter valid marks please")
    
if(marks<=100 and marks>=90):
    print("Your Grade is : Ex")

elif(marks<=89 and marks>=80):
    print("Your Grade is : A")

elif(marks<=79 and marks>=70):
    print("Your Grade is : B")

elif(marks<=69 and marks>=60):
    print("Your Grade is : C")

elif(marks<=59 and marks>=50):
    print("Your Grade is : D")

elif(marks<=49 and marks>=40):
    print("Your Grade is : E")

elif(marks<=39 and marks>=0):
    print("Your Grade is : F")