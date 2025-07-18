#hollow Rhombus
n = int(input("Enter the N value: "))
a = 0
for i in range(1,n+1):
    if i != 1 and i != n:
        b = n-2
        print("  " * a + " * ", "   " * b + " *")
        a += 1
    elif i == 1:
        print("*  " * n)
    elif i == n:
        print("  " * a + " * " * n)
