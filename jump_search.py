"""
This program implements the use of jump search on an array.
"""
import math


def jump_search(array, match, elements):
    step = math.sqrt(elements)
    prev = 0
    while array[int(min(step, elements) - 1)] < match:
        prev = step
        step += step
        if prev >= elements:
            return False

    while array[int(prev)] < match:
        prev += 1

        if prev == min(step, elements):
            return False

    if array[int(prev)] == match:
        return True


arr = []

n = int(input('Enter the number of elements in the array: '))

for i in range(n):
    arr.append(int(input('Enter array element: ')))

x = int(input('Enter the element you want to search: '))

arr.sort()

pos = 0
for i in range(len(arr)):
    if arr[i] == x:
        pos = i

result = jump_search(arr, x, n)

if result:
    print('The element is present at position: ', pos)
else:
    print('The element is not present.')

input()
