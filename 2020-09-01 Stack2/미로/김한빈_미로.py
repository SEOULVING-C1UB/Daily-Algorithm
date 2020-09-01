import sys

def dfs(start):
    s = []
    s.append(start)
    result = 0
    while len(s) != 0:
        V = s.pop()
        if not visited[V[0]][V[1]]:
            visited[V[0]][V[1]] = 1
            for dr,dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                if (arr[V[0] + dr][V[1] + dc] == '0') and (visited[V[0] + dr][V[1] + dc] == 0):
                    new = [V[0] + dr, V[1] + dc]
                    s.append(new)
                elif arr[V[0] + dr][V[1] + dc] == '3':
                    result = 1
                    break
    print(result)

sys.stdin = open('미로.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=' ')
    N = int(input())
    arr = ['1' + input() + '1' for _ in range(N)]
    arr.insert(0, '1' * (N + 2))
    arr.append('1' * (N + 2))

    for r in range(len(arr)):
        for c in range(len(arr[4])):
            if arr[r][c] == '2':
                r_S, c_S = r, c

    visited = [[0] * (N + 2) for _ in range(N + 2)]
    dfs([r_S, c_S])

