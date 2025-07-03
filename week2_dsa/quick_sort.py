import time
start_time = time.time()
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        # print("partition", arr)
        quick_sort(arr, low, pivot_index - 1)
        # print("1", arr)
        quick_sort(arr, pivot_index + 1 ,high)
        # print("2", arr)
    return arr
def partition(arr, low, high):
    pivot_index = arr[high]
    k = low
    for i in range(low, high):
        if arr[i] < pivot_index:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
    arr[k], arr[high] = arr[high], arr[k]
    return k
arr = [8,7,6,5,4,3,2,1]
# arr = list(map(int, input("Enter the elements: ").split()))
print(quick_sort(arr, 0, len(arr) - 1))
print(time.time())
