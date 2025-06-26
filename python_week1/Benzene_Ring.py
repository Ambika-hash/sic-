#Benzene Ring (C6H6) Hexagon
n = int(input("Enter the N value (>=3): "))
if n < 3:
    print("Please enter a value of N >= 3")
else:
    for i in range(n):
        spaces = " " * (n - i - 1)
        if i == 0:
            print(spaces + "#")
        else:
            print(spaces + "#" + " " * (2 * (n + i - 1) - 1) + "#")
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        if i == 0:
            print(spaces + "#")
        else:
            print(spaces + "#" + " " * (2 * (n + i - 1) - 1) + "#")
