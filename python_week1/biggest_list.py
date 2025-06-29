#Find smallest and biggest elements in an list of n numbers.
a = list(input("Enter the list: "))
max1 = a[0]
for i in a:
    if max1 < i:
        max1 = i
print(max1)
print(max(a))
print(min(a))