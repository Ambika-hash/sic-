def check_arrangement(total_array, boys, girls):
    if total_array[0::2] == sorted(boys) or total_array[0::2] == sorted(girls):
        return "Yes"
    else:
        return "No"
n = int(input("Number of test cases: "))
for i in range(n):
    total_stu = int(input("Number of boys and girls in the class: "))
    boys = list(map(int, input("Enter the height of boys: ").split()))
    girls = list(map(int, input("Enter the height of girls: ").split()))
    output = []
    total_array = boys + girls
    total_array.sort()
    output.append(check_arrangement(total_array, boys, girls ))
print(output)
    
    
