"""This program counts the elements of a list
If all the elements are unique it returns False
and is elements occur twice it returns True"""


def element_count(arr1):
    for i in arr1:
        if arr1.count(i) != 2:
            return False
    return True


arr = []

num = int(input("Enter the number of elements in the array: "))

for j in range(num):
    arr.append(int(input("Enter array element: ")))

print(element_count(arr))

input()
