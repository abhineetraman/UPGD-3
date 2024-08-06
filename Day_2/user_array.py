n = int(input("ENter the number of elements of the Array: "))

l = []

for i in range(1, n+1):
    x = int(input(f"Enter the {i} element: "))
    l.append(x)

print(l)