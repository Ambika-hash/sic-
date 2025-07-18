def backtrack(candidates, target, path, index):
    if target == 0:
        result.append(path[:])
        return
    if target < 0:
        return
    for i in range(index, len(candidates)):
        path.append(candidates[i])
        backtrack(candidates, target - candidates[i], path, i)
        path.pop()

candidates = list(map(int, input().split()))
target = int(input())
result = []
backtrack(candidates, target, [], 0)
print(result)
