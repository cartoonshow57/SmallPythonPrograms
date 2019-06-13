"""This program takes a list and an integer and replicates each array element
by integer times"""

def replicate_n_times(lst, n):
    lst1 = []
    for i in lst:
        if i not in lst1:
            for j in range(n):
                lst1.append(i)
    return lst1


lst = []

num = int(input("Enter the number of elements in the array: "))

for k in range(num):
    lst.append(int(input("Enter array element: ")))

n = int(input("How many times should the elements be replicated? "))

print("Entered array is as: ", lst)

print("Array after replicating elements: ", replicate_n_times(lst, n))

input()
