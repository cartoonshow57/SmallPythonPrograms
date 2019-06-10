"""This program converts Degree Celsius to Degree Fahrenheit using List Comprehension"""

def deg_to_fah(Dehrees):
    Fahrenheit = [(x * (9 / 5) + 32) for x in Degrees]
    return Fahrenheit


Degrees = []

n = int(input("Enter number of temperatures in Degrees: "))

for i in range(n):
    Degrees.append(float(input("Enter Temperature in Degree Celsius: ")))

print("Temperatures entered in Degree Celsius are:", Degrees)

print("Temperatures in Degree Fahrenheit comes out to be:", deg_to_fah(Degrees))

input()
