# This program splits a given array and adds the first part at the end


def split_arr(arr1, k1):
    new_arr = []
    req_arr = []
    count = 0
    while count < k1:
        element = arr1.pop(0)
        new_arr.append(element)
        count += 1
    req_arr = arr1 + new_arr
    return req_arr


arr = []

n = int(input("Enter the number of elements to be put in the array: "))

for i in range(n):
    arr.append(int(input("Enter array element: ")))

k = int(input("Enter from which element you want to split the array: "))

print("The given array was:", arr)

print("The array after split comes out as:", split_arr(arr, k))

input()
