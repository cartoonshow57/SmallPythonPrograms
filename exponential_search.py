"""
This program finds an element in a sorted array
"""


def binary_search(arr, low, high, element):
    if high >= low:
        mid = int((low + high) / 2)

        if arr[mid] == element:
            return mid

        if arr[mid] > element:
            return binary_search(arr, low, mid - 1, element)

        return binary_search(arr, mid + 1, high, element)

    return False


def exponential_search(arr, length, element):
    if arr[0] == element:
        return 0

    i = 1

    while i < length and arr[i] < element:
        i *= 2

    return binary_search(arr, i / 2, min(i, length), element)


array = []

elements = int(input('Enter the number of elements in the array: '))

for i in range(elements):
    array.append(int(input("Enter array element: ")))

array.sort()

x = int(input('Enter element to search: '))

result = exponential_search(array, elements, x)

if result:
    print('The element is present at index: ', result)
else:
    print('The element is not present.')

input()
