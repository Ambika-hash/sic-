def subset_sum(arr, n, total):
    if total == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > total:
        return subset_sum(arr, n-1, total)
    return subset_sum(arr, n-1, total) or subset_sum(arr, n-1, total - arr[n-1])

arr = list(map(int, input().split()))
target = int(input())
print(subset_sum(arr, len(arr), target))
