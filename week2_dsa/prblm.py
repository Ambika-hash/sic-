noOfeReq = int(input("E: "))
reqs = list(map(int, input("Enter the digits: ").split()))
server1 = reqs[0::2]
print(sum(server1))
