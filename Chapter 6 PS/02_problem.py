marks1 = int(input("Enter 1st subject marks :"))
marks2 = int(input("Enter 2nd subject marks :"))
marks3 = int(input("Enter 3rd subject marks :"))

total_percentage = (marks1 + marks2 + marks3)/3

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulation you passed the exam ", total_percentage)

else:
    print("You failed, Better luck next time", total_percentage)
