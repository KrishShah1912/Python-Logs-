# sum(n) = sum(n-1) + n

def sum(n):
    
    if(n==1):

        return 1
    
    else:

        c = sum(n-1) + n
        return c
    
n = int(input("Enter the natural number :"))

print(f"The sum of the first {n} natural number  : {sum(n)}")