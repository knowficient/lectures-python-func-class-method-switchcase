def carfuel(distance,fuel):
    kmpl = round((distance/fuel),2)
    lp100k = round((fuel*100/distance),2)
    return kmpl, lp100k

mileage, efficiency = carfuel(800, 60)
print("Mileage =", mileage,"kmpl")
print("Efficiency =", efficiency, "litres per 100km")
