class car(object):
    """
    This class creates instance of cars
    """
    def __init__(self,c,m):
       self.company = c
       self.mileage = m
    def salutation(self):
       print(f"The {self.company} car mileage is about {self.mileage} kmpl")
