"""This program takes an array and returns another array
which states whether a given number was prime or not"""


def prime_or_not(arr1):
    new_arr = []
    for i in arr1:
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    new_arr.append(False)
                    break
            else:
                new_arr.append(True)
    return new_arr


arr = []

num = int(input("Enter total number of elements in the array: "))

for k in range(num):
    arr.append(int(input("Enter array element: ")))

print("The given array is", arr)

print(prime_or_not(arr))

input()
