"""This program takes an array as input
and returns a list without any negative elements"""


def remove_negative(arr):
    positive_arr = []
    for i in arr:
        if i < 0:
            continue
        else:
            positive_arr.append(i)
    return positive_arr


arr = []

num = int(input("Enter number of elements in the array: "))

for k in range(num):
    arr.append(int(input("Enter array element: ")))

print("The given array is:")
print(arr)
print("After removing negative elements: ")
print(remove_negative(arr))

input()
