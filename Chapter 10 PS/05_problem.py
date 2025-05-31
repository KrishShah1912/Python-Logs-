from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo= trainNo

    def book(self, fro , to):
        print(f"Your ticket is booked successfully for train number : {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train number: {self.trainNo} is running on time")

    def getfare(self, fro , to):
        print(f"Ticket fare in train number : {self.trainNo} from {fro} to {to} is {randint(1111,9999)}inr")

t= Train(int(input("Enter the train number to check it's details :")))

t.book((input("Enter it's starting point :")), input("Enter it's destination :"))

t.getstatus()

t.getfare((input("Enter it's starting point :")), input("Enter it's destination :"))