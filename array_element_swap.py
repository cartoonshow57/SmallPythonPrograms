"""
This program swaps array elements fromm positions which the user inputs
"""


def element_swap(arr1, pos3, pos4):
    arr1[pos3], arr1[pos4] = arr1[pos4], arr1[pos3]
    return arr1


arr = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter array element: ")))

pos1, pos2 = int(input("Enter the index of first element to swap:")), int(input("Enter the second index: "))

print("The given array is:", arr)

print("Array after swapping becomes:", element_swap(arr, pos1, pos2))

input()
