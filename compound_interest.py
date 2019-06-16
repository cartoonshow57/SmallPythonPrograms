# This program take Principle, Rate and Time as input and calculates Compound Interest.

p = int(input("Enter the Principle amount: "))
r = float(input("Enter the Rate of Interest: "))
t = int(input("Enter the Time period: "))


def compound_interest(p1, r1, t1):
    compound_int = p1 * (1 + r1 / 100) ** t1
    return compound_int


print("The Compound Interest for the given values is ", compound_interest(p, r, t))
input()
