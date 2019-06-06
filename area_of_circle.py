# This program takes radius as input and calculates the area

def area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area


radius = int(input("Enter the radius of the circle: "))
print("The radius of the circle with radius",radius,"is",area(radius))
input()
