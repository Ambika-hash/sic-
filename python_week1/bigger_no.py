#Given a number, find very next possible bigger number that has all 
# the digits of the given number.
a = input("Enter the number: ")
l = []
for i in range(len(a)):
    f = a[i]
    w = a[:i] + a[i+1:]
    l.append(f + w)
print(l)

int_list = [int(x) for x in l]
s = sorted(int_list)
print(s)
i = s.index(int(a))
print(s[i+1])