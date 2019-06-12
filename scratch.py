# This program raises 5 fro 0 till the power of the number entered

num = int(input("Enter a number: "))
if num >= 0:
    for i in range(num + 1):
        print(5 ** i)
else:
    print("Enter a positive number.")

input()
