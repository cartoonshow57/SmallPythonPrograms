def fact_of_num(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact_of_num(num - 1)
print("The factorial of 5 is ",fact_of_num(5))
input()