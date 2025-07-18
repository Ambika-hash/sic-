#4. Print the Prime numbers in decreasing order between m and n (m < n)
start_point = int(input("Enter the beggining of the range: "))
end_point = int(input("Enter the last point of the range: "))
print("The prime number in range {} to {} is: ".format(start_point, end_point), end = " ")
for i in range(end_point, start_point, -1):
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end = " ")
    elif i == 2:
        print(i, end = " ")
    
