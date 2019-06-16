"""This program takes an array
and deletes the first and last element of the array"""


def remove_element(arr1):
    del arr1[0]
    del arr1[-1]
    return arr1


arr = []

n = int(input("Enter number of elements in the list: "))

for i in range(n):
    arr.append(int(input("Enter array element: ")))

print("The given list is: ")
print(arr)

print("After removing first and last element: ")
print(remove_element(arr))

input()
