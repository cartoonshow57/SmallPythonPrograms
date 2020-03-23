"""
This program searches for a given element in an array using linear search
"""


def linear_search(arr, ele):
    position = 0
    flag = False
    while position < len(arr) and not flag:
        if arr[position] == ele:
            flag = True
        else:
            position += 1
    return flag


array = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    array.append(int(input("Enter array element: ")))

num = int(input("Enter the number to search: "))

if linear_search(array, num):
    print("The element is present.")
else:
    print("The element is not present.")

input()
