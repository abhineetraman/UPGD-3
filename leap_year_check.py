#input the year

year = int(input("Enter the year:"))
#check for leap year and print the output

if year%4 != 0:
    print("Not a leap year")
elif (year%4 == 0) and ((year%100 != 0) or (year%400 == 0)):
    print("It is a leap year")
else:
    print("It is not a leap year")
