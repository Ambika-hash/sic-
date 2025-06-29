n = int(input("Enter the N value: "))
# for i in range(1,n+1):
#     if i != 1 and i != n:
#         b = n-2
#         print(" * ", "   " * b + "*")
#     elif i == 1 or i == n:
#         print(" * " * n)

if n < 3:
    print("Please enter a number >= 3")
else:
    a = 0
    b = n - 2
    for i in range(n // 2):
        if i == 0:
            print(" * " * n)
        # elif i == 1:
        #     print("   " * a + " * " + "   " * b + " * " + "   " * a )
        else:
            print(" * " , "   " * a + " * " + "   " * b + " * " + "   " * a , " * ")
        a += 1
        b -= 2
    if n % 2 == 1:
        print(" * " , "   " * (n // 2) + " o " , " * ")
    else:
        print(" * " , "   " * (n // 2) + "   " , " * ")
    a -= 1
    b += 2
    for i in range(n // 2 - 1, -1, -1):
        if i == 0:
            print(" * " * n)
        # elif i == (n // 2 - 2):
        #     print("   " * a + " * " + "   " * b + " * " + "   " * a)
        else:
            print(" * " , "   " * a + " * " + "   " * b + " * " + "   " * a , " * ")
        a -= 1
        b += 2
