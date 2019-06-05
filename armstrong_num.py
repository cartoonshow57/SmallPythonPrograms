def arm_num(num):
    sum = 0
    while num >= 1:
        digit = num % 10
        sum = sum + digit ** 3
        num = num // 10
    return sum


num = int(input("Enter a number to check is its Armstrong or not: "))
if num == arm_num(num):
    print("The number ", num, " is Armstrong.")
else:
    print("The number ", num, "is not Armstrong.")

input()