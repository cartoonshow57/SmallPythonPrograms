# This program rotates the given array of num elements by d elements

def array_rotation(arr, d):
    test_arr = []
    new_arr = []
    for j in range(d):
        element = arr.pop()
        test_arr.append(element)
        test_arr.sort()
    new_arr = test_arr + arr
    return new_arr


arr = []

num = int(input("Enter the number of elements in the array: "))

for i in range(num):
    arr.append(int(input("Enter an array number: ")))

d = int(input("By how many elements should the array be rotated: "))

print("The given array is:", arr)
print("The array after rotation is:", array_rotation(arr, d))

input()
