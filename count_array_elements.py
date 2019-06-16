"""This program takes an array and couts the occurrenes of each element in the array"""


def count_element(arr1):
    lst = []
    for i in arr1:
        if i not in lst:
            lst.append(i)
            count = arr1.count(i)
            print(i, "occurs", count, "times.")
    return " "


arr = []

n = int(input("Enter the number of elements in the array: "))

for j in range(n):
    arr.append(int(input("Enter array element: ")))

print("The array is: ", arr)

print("Element Count: ")
print(count_element(arr))

input()
