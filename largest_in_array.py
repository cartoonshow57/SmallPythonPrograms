def largest_in_arr(arr):
    largest = 0
    for j in arr:
        if j > largest:
            largest = j
    return largest


arr = []

num = int(input("Enter the number of elements in array: "))

for i in range(num):
    arr.append(int(input("Enter array element: ")))

print("The largest number in the given array is:", largest_in_arr(arr))

input()
