#Find sum of the Odd placed Even digits in the given number.
input_number = input("Enter the number: ")
sum = 0
for i in range(1, len(input_number), 2):
    if int(input_number[i]) % 2 == 0:
        sum += int(input_number[i])
print(sum)