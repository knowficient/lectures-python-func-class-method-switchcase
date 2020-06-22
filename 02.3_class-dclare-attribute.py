class car(object):
    """
    This class creates instance of cars
    """
    def __init__(self,c,m):
        self.company = c
        self.mileage = m
    def salutation(self):
        print(f"The {self.company} car mileage is about {self.mileage} kmpl")

bmwS7 = car('BMW',23)  # create a car object
bmwS7.horsepower = 101; print(bmwS7.horsepower)   # Add new attribute for an object on-the-fly
audiA8 = bmwS7; print(audiA8.mileage)             # Assign values to new object