# This program prints a certain term of the fibonacci series


def fibonacci(num1):
    if num1 == 1:
        return 0
    elif num1 == 2:
        return 1
    elif num1 > 2:
        return fibonacci(num1 - 1) + fibonacci(num1 - 2)
    else:
        return "Invalid Input"


# Take user input
num = int(input("Enter the term you wish to know in the Fibonacci Series: "))

print("The value of", num, "th term in Fibonacci Series is:", fibonacci(num), ".")

input()
