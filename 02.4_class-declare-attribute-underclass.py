class car:
    size = "big"     # declare an attribute under a class
    def __init__(self,c,m):
        self.company = c
        self.mileage = m
    def salutation(self):
        print(f"The {self.company} car mileage is about {self.mileage} kmpl")

print(car.size)
camry = car("Toyota",31)
print(camry.size)
