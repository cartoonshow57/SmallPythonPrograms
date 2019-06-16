# This programs checks if a number is prime or not


def prime_or_not(num1):
    flag = 0
    if num1 > 1:
        for i in range(2, num1):
            if (num1 % i) == 0:
                break
        else:
            flag += 1
    return flag


num = int(input("Enter a number to check if its prime or not: "))
if prime_or_not(num) == 1:
    print("The number", num, "is Prime.")
else:
    print("The number", num, "is not Prime.")

input()
