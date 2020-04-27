"""
This program implements the use of Fibonacci search to find an element in a sorted array
"""


def fibonacci_search(array, element, size):
    fibM2 = 0
    fibM1 = 1
    fibM = fibM2 + fibM1

    while fibM < size:
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1

    offset = -1

    while fibM > 1:
        index = min(offset + fibM1, size - 1)
        if array[index] < element:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = index

        elif array[index] > element:
            fibM = fibM2
            fibM1 = fibM1 - fibM
            fibM2 = fibM - fibM1

        else:
            return index

    if fibM1 & array[offset + 1 == element]:
        return offset + 1

    return False


arr = []

n = int(input('Enter the number of elements in the array: '))

for i in range(n):
    arr.append(input('Enter array element: '))

arr.sort()

x = int(input('Enter the element to be searched: '))

result = fibonacci_search(arr, x, n)

if result:
    print('The element is present at index: ', result)
else:
    print('The element is not present.')

input()
