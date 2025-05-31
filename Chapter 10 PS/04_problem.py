class calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of the number is {self.n*self.n}")

    def cube(self):
        print(f"The cube of the number is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square root of the number is {(1/2) *self.n}")

    @staticmethod
    def hello():
        print("Hello there.......")
        print("Your requirement will be display below ")


n =int(input("Enter the number :"))

a= calculator(n)
a.hello()
a.square()
a.cube()
a.squareroot()