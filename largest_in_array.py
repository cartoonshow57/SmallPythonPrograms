# This program prints the largest in a given array


def largest_in_arr(arr1):
    largest = 0
    for j in arr1:
        if j > largest:
            largest = j
    return largest


arr = []

num = int(input("Enter the number of elements in array: "))

for i in range(num):
    arr.append(int(input("Enter array element: ")))

print("The largest number in the given array is:", largest_in_arr(arr))

input()
