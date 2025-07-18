#3. Count number of Prime digits in a number
input_number = input("Enter the number: ")
count = 0
for i in range(len(input_number)):
    if int(input_number[i]) > 2:
        for j in range(2, int(input_number[i])):
            if int(input_number[i]) % j == 0:
                break
        else:
            count += 1
    elif int(input_number[i] ) == 2:
        count += 1
print("The number of prime numbers in", input_number, "is: ", count)