"""This program checks if the given array is monotonic or not
returns True if array is monotonic increasing or decreasing
else returns False"""


def monotonic_array(arr1):
    return all(arr1[i] >= arr1[i + 1] for i in range(len(arr1) - 1)) or (
        all(arr1[i] <= arr1[i + 1] for i in range(len(arr1) - 1)))


arr = []

n = int(input("Enter the number of elements in the array: "))

for j in range(n):
    arr.append(int(input("Enter array element: ")))

print("The given array is:", arr)

print(monotonic_array(arr))

input()
