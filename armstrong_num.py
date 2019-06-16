# This program takes a number as input and checks if it is Armstrong or not


def arm_num(num1):
    sum1 = 0
    while num1 >= 1:
        digit = num1 % 10
        sum1 = sum1 + digit ** 3
        num1 = num1 // 10
    return sum1


num = int(input("Enter a number to check is its Armstrong or not: "))
if num == arm_num(num):
    print("The number ", num, " is Armstrong.")
else:
    print("The number ", num, "is not Armstrong.")

input()
