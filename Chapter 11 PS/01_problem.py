class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
        
# For 2D vector
m = int(input("Enter the first vector number/dimension :"))
n = int(input("Enter the second vector number/dimension :"))

# For 3D vector
x = int(input("Enter the first vector number/dimension :"))
y = int(input("Enter the second vector number/dimension :"))
z = int(input("Enter the third vector number/dimension :"))
a = TwoDvector(m,n)
b = ThreeDvector(x,y,z)
a.show()
b.show()

