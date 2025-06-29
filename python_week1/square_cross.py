# n = int(input("Enter the N value: "))

# if n < 3:
#     print("Please enter a number >= 3")
# else:
#     a = 0
#     b = n - 2
#     for i in range(n // 2):
#         if i == 0:
#             print(" * " * n)
#         else:
#             print(" * " + "   " * a + "*" + "   " * b + "*" + "   " * a + " * ")
#         a += 1
#         b -= 2

#     # Center row with the 'o' in middle
#     if n % 2 == 1:
#         print(" * " + "   " * (n // 2) + "o" + "   " * (n // 2) + " * ")
#     else:
#         print(" * " + "   " * (n // 2) + "o" + "   " * (n // 2) + " * ")

#     a -= 1
#     b += 2
#     for i in range(n // 2 - 1, -1, -1):
#         if i == 0:
#             print(" * " * n)
#         else:
#             print(" * " + "   " * a + "*" + "   " * b + "*" + "   " * a + " * ")
#         a -= 1
#         b += 2
n = int(input("Enter the N value: "))
if n < 3:
    print("Please enter a number >= 3")
else:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(" * ", end="")
            elif i == j or j == n - i - 1:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()
