def one():
    return "Level 1"
def two():
    return "Level 2"
def three():
    return "Level 3"

switcher={
    1:one,
    2:two,
    3:three
}

def carpark(c):
    func = switcher.get(c, lambda:"Invalid level")
    return func()

print(carpark(2))
switcher[2] = three
print(carpark(2))
