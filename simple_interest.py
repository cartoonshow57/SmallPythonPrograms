p = int(input("Enter the Principle amount: "))
r = int(input("Enter the Rate of interest: "))
t = int(input("Enter the total Time period: "))
def simple_interest(p1, r1, t1):
    simple_int = (p * r * t) / 100
    return simple_int

print("The simple Interest for the given values is ", simple_interest(p, r, t))
input()