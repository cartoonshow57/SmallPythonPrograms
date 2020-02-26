"""This program counts the elements of a list
If all the elements are unique it returns True
and is elements occur twice it returns False"""


def element_count(arr1):
    for i in arr1:
        if arr1.count(i) != 2:
            return True
    return False


arr = []

num = int(input("Enter the number of elements in the array: "))

for j in range(num):
    arr.append(int(input("Enter array element: ")))

print(element_count(arr))

input()
