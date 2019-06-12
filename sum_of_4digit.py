# This program inputs a number and prints the sum of its digits

num = eval(input("Enter a 4-digit number : "))
r1 = num % 10
q1 = num // 10
r2 = q1 % 10
q2 = q1 // 10
r3 = q2 % 10
q3 = q2 // 10
r4 = q3
sum_num = r1 + r2 + r3 + r4
print("The sum of the digits is :-\n", r1, "\n", r2, "\n", r3, "\n", r4, "\n", sum_num)
input()
