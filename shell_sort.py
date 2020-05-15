"""
Implementation of Shell sort sorting technique
"""


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


array = list(map(int, input('Enter array elements: ').strip().split()))

print('Given array: ', array)

print('Sorted array: ', shell_sort(array))

input()
