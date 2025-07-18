def permute(s, l, r):
    if l == r:
        print(''.join(s))
        return
    for i in range(l, r + 1):
        s[l], s[i] = s[i], s[l]
        permute(s, l + 1, r)
        s[l], s[i] = s[i], s[l]

s = list(input())
permute(s, 0, len(s)-1)
