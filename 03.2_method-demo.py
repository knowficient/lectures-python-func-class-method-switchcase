class demo:
    def __init__(thisobj,b):  # replace "thisobj" instead of "self"
        thisobj.brand = b

car1 = demo("Audi")
print(car1.brand)
