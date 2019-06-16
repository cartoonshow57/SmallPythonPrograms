# This program takes a range and prints all the prime numbers in that range


def prime_nums(start1, end1):
    for i in range(start1, end1 + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)
    return None


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("The Prime numbers between", start, "and", end, "are: \n")
prime_nums(start, end)

input()
