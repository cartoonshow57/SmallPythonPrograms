# A progra to sum the cubes of numbers from zero till that the input number

def sum_of_n_cubes(num):
    count = 0
    if num < 0:
        return "No negative numbers."
    elif num == 0:
        return "The sum is 0."
    else:
        for i in range(num + 1):
            s = i * i * i
            count += s
    return count


num = int(input("Enter a number to check the sum of cubes till that number: "))

print(sum_of_n_cubes(num))

input()
