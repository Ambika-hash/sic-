#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2
input_n = int(input("Enter the range: "))
print("The fibonacci series is: ", end = " ")
if input_n > 2:
    a ,b = 1, 2
    print(a, b, end = " ")
    for i in range(input_n):
        c = a + b
        a, b = b, c
        print(c, end = " ")
elif input_n == 1:
    print(1)
else:
    print("1 2")
