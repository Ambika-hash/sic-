n = int(input("Number of oranges: "))
oranges = list(map(int, input("Enter the number of oranges: ").split()))
k = 0
for i in range(0, n-1):
    if oranges[i] <= oranges[n-1]:
        oranges[i], oranges[k] = oranges[k], oranges[i]
        k += 1
oranges[k], oranges[n-1] = oranges[n-1], oranges[k]
print(oranges)
    