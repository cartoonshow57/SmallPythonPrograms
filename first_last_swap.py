"""This program interchanges the first and last element in an array"""


def array_swap(arr1):
    first = arr1.pop(0)
    last = arr1.pop()
    arr1.append(first)
    arr1.insert(0, last)
    return arr1


arr = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("The given array is:", arr)

print("Array after swapping first and last:", array_swap(arr))

input()
