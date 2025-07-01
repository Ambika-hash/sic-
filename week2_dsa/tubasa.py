T = int(input())  

for _ in range(T):
    N, current_player = input().split()
    N = int(N)
    current_player = int(current_player)

    stack = [] 

    for _ in range(N):
        line = input().split()
        if line[0] == 'P':
            stack.append(current_player)
            current_player = int(line[1])
        elif line[0] == 'B':
            current_player = stack.pop()

    print(f"Player {current_player}")
