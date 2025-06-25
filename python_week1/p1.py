# a = int(input("enter first number :"))
# b = int(input("enter first number :"))
# c = int(input("enter first number :"))
# # if a<b and a<c:
# #     print(a, "is the smallest")
# # elif b<c and b<a:
# #     print(b, "number is the smallest")
# # else:
# #     print(c, "number is the smallest")
# print(min(a, b, c), "is the smallest of the three")
a = int(input("Check if a +ve integer is Perfect square: "))
b = int(a**0.5)
if (b**2 == a):
    print(a, "is Perfect square")
else:
    print(a, "is not Perfect square")

