def binary_search(search_ele, elements):
    l = 0
    h = len(elements) - 1
    while l <= h:
        mid = (l + h) // 2
        if search_ele == elements[mid]:
            return mid
        elif search_ele > elements[mid]:
            l = mid + 1
        else:
            h = mid - 1
    return -1
search_ele = int(input("Enter the search element: "))
elements = list(map(int, input("Enter the elements: ").split()))
print(binary_search(search_ele, elements))
