def generate(n, open, close, s):
    if len(s) == 2 * n:
        result.append(s)
        return
    if open < n:
        generate(n, open+1, close, s + "(")
    if close < open:
        generate(n, open, close+1, s + ")")

n = int(input())
result = []
generate(n, 0, 0, "")
print(result)
