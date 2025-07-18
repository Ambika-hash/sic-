#. Find sum of list elements
def recursive_sum(lst):
    if not lst:  
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])
nums = [1, 2, 3, 4, 5]
print("Sum:", recursive_sum(nums))
