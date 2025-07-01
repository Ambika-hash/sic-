total_elements = int(input("Enter the total elements: "))
main_list = list(map(int, input("Enter the source elements: ").split()))
reached = list(map(int, input("Enter the destination elements: ").split()))
sorted(main_list)
sorted(reached)
missed = []
i = 0
j = 0
while i < len(main_list) and j < len(reached):
    if main_list[i] == reached[j]:
        i += 1
        j += 1
    else:
        missed.append(main_list[i])
        i += 1
if i != len(main_list):
    missed.extend(main_list[i:])
print(missed)