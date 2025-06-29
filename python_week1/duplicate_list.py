#Remove the duplicates in a list of size n
a = list(input("Enter the list: "))
l = []
for i in a:
    if i in l:
        pass
    else:
        l.append(i)
print("The list with no duplicate values is :", l)
