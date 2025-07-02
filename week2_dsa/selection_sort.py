list1 = list(map(int, input("Enter the list: ").split()))
N = len(list1)
for i in range(1, N):
	element = list1[i-1]
	position = i-1
	for j in range(i-1, N):
		if list1[j] < element:
			element = list1[j]
			position = j
	list1[position], list1[i-1] = list1[i-1], list1[position]
print(list1)