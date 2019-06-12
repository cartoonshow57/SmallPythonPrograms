# A program to sum the squares of all the numbers between zero and the input number

def sum_of_n(num):
    count = 0
    if num >= 1:
        for i in range(num + 1):
            count += i ** 2
    elif num == 0:
        print("The sum is 0.")
    else:
        print("No negative numbers please.")
    return count


num = int(input("Enter a number to add the squares till that number: "))

print("The value of sum returned is:", sum_of_n(num))

input()
