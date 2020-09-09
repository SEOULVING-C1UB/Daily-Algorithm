import sys

def dfs(start):
    s = []
    s.append(start)
    result = []
    while len(s) != 0:
        V = s.pop()
        if not visited[V[0]][V[1]]:
            visited[V[0]][V[1]] = 1
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                check = 0
                if (arr[V[0] + dr][V[1] + dc] == '0') and (visited[V[0] + dr][V[1] + dc] == 0):
                    new = [V[0] + dr, V[1] + dc]
                    s.append(new)
                    result.append(1)
                    check = 1
                elif arr[V[0] + dr][V[1] + dc] == '3':
                    result.append(1)
                    break
            if check == 0:
                result.append(0)
    print(result)

def bfs(start):
    q = []
    q.append(start)
    result = 0
    while len(q) != 0:
        r, c = q.pop(0)
        if arr[r][c] == '3':
            print(visited[r][c])
            break
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            if (arr[r + dr][c + dc] == '0') and (visited[r + dr][c + dc] == 0):
                visited[r + dr][c + dc] = visited[r][c] + 1
                new = [r + dr, c + dc]
                q.append(new)
                result += 1
    print(visited[r][c])
    print(result)



sys.stdin = open('미로의 거리.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N = int(input())
    arr = ['1' + input() + '1' for _ in range(N)]
    arr.insert(0, '1' * (N + 2))
    arr.append('1' * (N + 2))

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == '2':
                r_S, c_S = r, c

    visited = [[0] * (N + 2) for _ in range(N + 2)]
    bfs([r_S, c_S])