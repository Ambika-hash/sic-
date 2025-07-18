#B. Equi lateral Triangle
n = int(input("Enter the N value: "))
a = (2 * n - 1)//2
for i in range(1, 2 * n, 2):
    print(" " * a + "*" * i)
    a -= 1
