# This program takes radius as input and calculates the area


def area(radius1):
    pi = 3.14
    area1 = pi * radius1 ** 2
    return area1


radius = int(input("Enter the radius of the circle: "))
print("The radius of the circle with radius", radius, "is", area(radius))
input()
