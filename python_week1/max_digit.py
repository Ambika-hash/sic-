#Find biggest digit in a number
input_number = input("Enter the number: ")
max1 = int(input_number[0])
for i in range(len(input_number)):
    if max1 < int(input_number[i]):
        max1 = int(input_number[i])
print("The maximum digit of", input_number, "is", max1)

