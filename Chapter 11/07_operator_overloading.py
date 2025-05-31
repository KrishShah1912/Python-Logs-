class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n + num.n
    
n= Number(int(input("Enter the number :")))
m=Number(int(input("Enter the number :")))

print(n+m)