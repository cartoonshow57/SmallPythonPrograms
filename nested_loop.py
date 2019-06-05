print("Nested loop example")
print("-------------------------------")
for i in range(1, 4, 1):
    for j in range(1, 1001, 999):
        print(format(i * j, "8d"), end="")
    print()
print("EOP")
input()