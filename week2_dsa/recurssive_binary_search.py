def binary_search(low, high, search_ele, elements):
    if low <= high:
        return -1
    else:
        mid = (low + high) // 2
        if search_ele == elements[mid]:
            return mid
        elif elements[mid] > search_ele:
            binary_search(mid + 1 , high, search_ele, elements)
        else:
            binary_search(low , mid - 1, search_ele, elements)



search_ele = int(input("Enter the search element: "))
elements = list(map(int, input("Enter the elements: ").split()))
low = 0
high = len(elements) - 1
print(binary_search(low, high, search_ele, elements))