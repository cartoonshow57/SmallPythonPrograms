# This program prints the roots of a quadratic equation by taking all the coefficients


def eval_quad_equation(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    if a > 0:
        root1 = ((- b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        root2 = ((- b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        print("The roots are - ", root1, " and ", root2)
    else:
        print("Enter valid values of the equation.")


eval_quad_equation(4, 3, 1)

input()
