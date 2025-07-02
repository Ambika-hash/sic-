list1 = list(map(int, input("Enter the list: ").split()))
N = len(list1)
for i in range(1, N-1):
	sorted = True # Assume the list is already sorted
	for j in range(0, N-1-i):
		if list1[j] > list1[j+1]:
			list1[j], list1[j+1] = list1[j+1], list1[j]
			sorted = False
	if(sorted):
		break
print(list1)