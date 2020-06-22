class demo1:            # class with methods
    def __init__(self,b,c):
        self.brand = b
        self.colour = c
    def salutation(self):
        print(self.colour, self.brand)
car1 = demo1("Audi","Red")
car1.colour = "Black"
car1.salutation()

def demo2(b,c):         # function
    print(c,b)
demo2("Audi","Red")
