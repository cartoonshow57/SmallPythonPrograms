"""
This program finds an element in the given array using binary search
"""


def binarysearch(arr, ele):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == ele:
            return True
        elif arr[mid] > ele:
            high = mid - 1
        else:
            low = mid + 1
    return False

array = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    array.append(int(input("Enter array element: ")))

array.sort()

num = int(input("Enter the element you wanna search: "))

if binarysearch(array, num):
    print("The element is present.")
else:
    print("The element is not present.")

input()
