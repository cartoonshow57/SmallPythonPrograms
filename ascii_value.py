# This program inputs a character and prints its ASCII value


def ascii_value(string1):
    a = ord(string1)
    return a


string = input("Enter a character to know its ASCII value: ")

print("The ASCII value of", string, "is", ascii_value(string))

input()
