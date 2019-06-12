"""This program takes a positive integer
and returns a list that contains first five multiples of that number"""

def list_of_multiples(num):
    Lst = []
    for i in range(1, 6):
        multiple = num * i
        Lst.append(multiple)
    return Lst


num = int(input("Enter a positive number: "))

print("The first five multiples of", num, "are", list_of_multiples(num))

input()
