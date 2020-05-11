"""
Implementation of merge sort
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftarr = arr[: mid]
        rightarr = arr[mid:]
        merge_sort(leftarr)
        merge_sort(rightarr)

        i = j = k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1

        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1

    return arr


array = list(map(int, input('Enter array elements: ').strip().split()))

print('Given array is: ', array)
print('Sorted array: ', merge_sort(array))

input()
