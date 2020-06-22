class Switcher(object):
    def level(self, x):
        method_name = "function_" + str(x)
        method = getattr(self, method_name, lambda: "Invalid")
        return method()
    def function_0(self):
        return "Level 0"
    def function_1(self):
        return "Level 1"
    def function_2(self):
        return "Level 2"

carpark = Switcher()
print(carpark.level(2))
print(carpark.level(4))
