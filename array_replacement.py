"""Given an array of n terms and an integer m, this program modifies
the given array as arr[i] = (arr[i-1]+1) % m and return that array"""

def array_modification(arr, m):
    test_arr = []
    index = 0
    for j in arr:
        s = (arr[index - 1] + 1) % m
        test_arr.append(s)
        index += 1
    return test_arr


arr = []

n = eval(input("Enter the number of elements in the array: "))

for i in range(n):
    arr.append(eval(input("Enter array element: ")))

m = eval(input("The modulo will be taken with which number? "))

print("The given array is:", arr)
print("The modified array comes out to be:", array_modification(arr, m))

input()
