# This program multiply all the numbers in an array and divide them by a number n


def array_multiplication(arr, n):
    product = 1
    for j in arr:
        product *= j
    print("The product of array elements is:", product)
    remainder = product % n
    print("The remainder comes out to be", remainder)


arr = []

num = int(input("Enter the number of elements in the array: "))

for i in range(num):
    arr.append(int(input("Enter array element: ")))

n = int(input("Enter the number which divides the product of array elements: "))

print("The given array is:", arr)

array_multiplication(arr, n)

input()
