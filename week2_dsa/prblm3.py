n = int(input("Enter the total number of inputs: "))
x = int(input("Enter the number of x elements: "))
y = int(input("Enter the number of y elements: "))
main_list =  list(map(int, input("Enter the digits: ").split()))    
if x + y == n and len(main_list) == n:
    main_list.sort()
print(main_list[y] - main_list[y - 1] - 1)