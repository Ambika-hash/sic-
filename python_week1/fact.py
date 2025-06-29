# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
    
# n = int(input("Enter the number: "))
# f = fact(n)
# print(n)
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
n = int(input("Enter the number: "))
f = fact(n)
print(f"Factorial of {n} is: {f}")