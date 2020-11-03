from collections import deque


def sol(r, c):
    global answer
    dp = [[INF for i in range(W)] for j in range(L)]
    dp[r][c] = 0
    q = deque([(r, c)])
    while q:
        y, x = q.popleft()
        maxi = dp[y][x]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < W and 0 <= ny < L:
                if maxi + 1 < dp[ny][nx] and MAP[ny][nx] == 'L':
                    dp[ny][nx] = maxi + 1
                    q.append((ny, nx))

    if maxi > answer:
        answer = maxi


L, W = map(int, input().split())
MAP = [list(input()) for _ in range(L)]
INF = float('inf')
answer = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for r in range(L):
    for c in range(W):
        if MAP[r][c] == 'L':
            sol(r, c)
print(answer)
