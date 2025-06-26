#C. Hollow Square
n = int(input("Enter the N value: "))
for i in range(1,n+1):
    if i != 1 and i != n:
        b = n-2
        print(" * ", "   " * b + "*")
    elif i == 1 or i == n:
        print(" * " * n)