n = int(input("Enter the N value (>= 3): "))

if n < 3:
    print("Please enter a number >= 3")
else:
    a = 0
    b = n - 2
    for i in range(n // 2):
        print(" " * a + "*" + " " * b + "*" + " " * a)
        a += 1
        b -= 2
    if n % 2 == 1:
        print(" " * (n // 2) + "*")
    else:
        print(" " * (n // 2) + " ")
    a -= 1
    b += 2
    for i in range(n // 2 - 1, -1, -1):
        print(" " * a + "*" + " " * b + "*" + " " * a)
        a -= 1
        b += 2
