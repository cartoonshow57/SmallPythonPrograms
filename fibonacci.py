# Define function to find nth fibonacci number
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)
    else:
        return "Invalid Input"


# Take user input
num = int(input("Enter the term you wish to know in the Fibonacci Series: "))

print("The value of", num, "th term in Fibonacci Series is:", fibonacci(num), ".")

input()
