# This program checks if a number belongs to the Fibonacci series


def check_perf_square(number):
    s = int(number ** 0.5)
    return s * s == number


def check_fib(num1):
    return check_perf_square(5 * num1 * num1 + 4) or check_perf_square(5 * num1 * num1 - 4)


num = int(input("Enter a number to check if it's Fibonacci or not: "))

if check_fib(num):
    print(num, "is a Fibonacci number.")
else:
    print(num, "is not a Fibonacci number.")

input()
