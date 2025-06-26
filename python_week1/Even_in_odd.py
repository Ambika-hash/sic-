#Find sum of the Even placed digits in the given number.
input_number = input("Enter the number : ")
sum = 0
for i in range(0, len(input_number), 2):
    sum += int(input_number[i])
print(sum)
