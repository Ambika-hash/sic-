coins = int(input("No. of gold coins in bag: "))
worth_coins = list(map(int, input("Enter the worth of coins: ").split()))
instruction, total = map(int, input("total ").split())
stack = []
t = 0
for i in range(instruction):
    instruct = input("Enter the instruction: ")
    if instruct == "Harry":
        stack.append(worth_coins[t])
        t += 1
    elif instruct == "Remove":
        del stack[-1]
if sum(stack) == total:
    print(len(stack))
else:
    print(-1)