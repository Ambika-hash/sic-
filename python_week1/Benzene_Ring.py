#Benzene Ring (C6H6) Hexagon
# n = int(input("Enter the N value (>=3): "))
n = 5
if n < 3:
    print("Please enter a value of N >= 3")
else:
    for i in range(n//2):
        spaces = " " * (n - i - 1)
        if i == 0:
            print(spaces + "# " * n)
        else:
            print(spaces + "# " + " " * (2 * (n + i - 1) - 1) + "# ")
    for i in range(n//2 + 1, 0, -1):
        spaces = " " * (n - i - 1)
        if i == 1:
            print(spaces + " #" * n)
        else:
            print(spaces + "#" + " " * (2 * (n + i - 1) - 1) + "#")
