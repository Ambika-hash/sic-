#Find sum of the series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
n = int(input("Enter N (term) value: "))
m = int(input("Enter the M value: "))
sum_of_term = 0
for i in range(m):
    numerator =  n**2**i
    denominator = 2 * i + 1
    sign = (-1)**i
    sum_of_term = numerator / denominator * sign
print(sum_of_term) 