# This is a program to write multipication for given input number

i = 1

num = int(input("Enter a number: "))

print("The multipication table for", num , "is")

while i<=10:
    print(num, "x", i, "=", num*i)
    i += 1