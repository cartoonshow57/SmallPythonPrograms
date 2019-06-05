def fib_num(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num > 2:
        return fib_num(num - 1) + fib_num(num - 2)


num = int(input("Enter the term in Fibonacci series you wish to multiply: "))

multiply_by = int(input("Enter how many times you want to multiply: "))

fibonacci1 = fib_num(num)

fibonacci2 = fibonacci1 * multiply_by

print("The", multiply_by, "\'th multiple of", fibonacci1, "is", fib_num(fibonacci2), "which appears at", fibonacci2, "\'th position.")

input()
