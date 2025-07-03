def selection_sort(list1, N):
	for i in range(1, N):
		sorted = True
		element = list1[i-1]
		position = i-1
		for j in range(i-1, N):
			if list1[j] < element:
				element = list1[j]
				position = j
				sorted = False
		list1[position], list1[i-1] = list1[i-1], list1[position]
		if sorted:
			break
	return list1
list1 = list(map(int, input("Enter the list: ").split()))
N = len(list1)
print(selection_sort(list1, N))