def sum_of_array(arr, n):
    total = sum(list(arr))
    return total


arr = []

n = int(input("Enter the number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter no. in array: ")))
print("The given array is,", arr)

print("The sum of given elements in the array is", sum_of_array(arr, n))

input()
