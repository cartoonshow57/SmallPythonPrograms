"""This program takes a positive integer
and returns a list that contains first five multiples of that number"""


def list_of_multiples(num1):
    lst = []
    for i in range(1, 6):
        multiple = num1 * i
        lst.append(multiple)
    return lst


num = int(input("Enter a positive number: "))

print("The first five multiples of", num, "are", list_of_multiples(num))

input()
