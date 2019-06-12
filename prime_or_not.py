# This programs checks if a number is prime or not

def prime_or_not(num):
    flag = 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
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
