class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print(f" Bow Bow !!!!")

x = dog()
x.bark()