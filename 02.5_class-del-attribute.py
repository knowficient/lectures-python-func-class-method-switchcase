class car:
    size = "big"
    def __init__(self,c,m):
        self.company=c
        self.mileage=m
    def salutation(self):
        print("Hello")

camry = car("Toyota",31)
del camry.mileage           #del an atrribute
print (camry.mileage)
