"""
This program swaps array elements fromm positions which the user inputs
"""


def element_swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


arr = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter array element: ")))

pos1, pos2 = int(input("Enter the index of first element to swap:")), int(input("Enter the second index: "))

print("The given array is:", arr)

print("Array after swapping becomes:", element_swap(arr, pos1, pos2))

input()
