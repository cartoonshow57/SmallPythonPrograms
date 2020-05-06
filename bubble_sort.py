"""
Implementation of bubble sort sorting technique
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array = list(map(int, input('Enter array element: ').split()))
print('Give array: ', array)
print('Sorted array: ', bubble_sort(array))

input()
