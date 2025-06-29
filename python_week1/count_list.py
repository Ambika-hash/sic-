#Find the frequency an element in a list of n elements.
a = list(input("Enter the list: "))
print(a)
l = []
for i in range(len(a)) :
    if (a[i] not in l):
        print("The count of ", a[i], "is ", a.count(a[i]))
        l.append(a[i])