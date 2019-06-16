# This program prints the sum of all the elements in an array


def sum_of_array(arr1):
    total = sum(list(arr1))
    return total


arr = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter no. in array: ")))
print("The given array is,", arr)

print("The sum of given elements in the array is", sum_of_array(arr))

input()
