#Benzene Ring (C6H6) Hexagon
n = int(input("Enter the N value (>=3): "))
if n < 3:
    print("Please enter a value of N >= 3")
else:
    for i in range(n//2):
        if i == 0:
            print(" " * (n - i - 1) + "# " * n)
        else:
            print(" " * (n - i - 1) + "#" + " " * (2 * (n + i - 1) - 1) + "# ")
    for i in range(n//2 + 1, 0, -1):
        if i == 1:
            print(" " * (n - i - 1) + " #" * n)
        else:
            print(" " * (n - i - 1) + "#" + " " * (2 * (n + i - 1) - 1) + "#")
