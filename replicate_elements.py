"""This program takes a list and an integer and replicates each array element
by integer times"""


def replicate_n_times(lst1, n1):
    lst2 = []
    for i in lst1:
        if i not in lst2:
            for j in range(n1):
                lst2.append(i)
    return lst2


lst = []

num = int(input("Enter the number of elements in the array: "))

for k in range(num):
    lst.append(int(input("Enter array element: ")))

n = int(input("How many times should the elements be replicated? "))

print("Entered array is as: ", lst)

print("Array after replicating elements: ", replicate_n_times(lst, n))

input()
