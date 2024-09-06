import math

def Area_calculation(r):
    return math.pi * r**(2.0)


r = float(input ('Enter the radius of the circle : '))
print("the area of the circle = " , Area_calculation(r))