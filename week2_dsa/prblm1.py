def Isroatated(org, rotat):
    temp = rotat * 2
    if temp.find(org) != -1:
        return 1
    else:
        return temp.find(org)
original = input("Enter the original word: ")
rotated = input("Enter the rotated word: ")
a = Isroatated(original, rotated)
print(a)
