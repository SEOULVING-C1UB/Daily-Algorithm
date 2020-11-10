# use pypy3
from collections import deque


def bfs(r, c):
    visited[r][c] = 1
    q = deque([(r, c)])
    group = {(r, c)}
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(A[ny][nx] - A[y][x]) <= R:
                    group.add((ny, nx))
                    q.append((ny, nx))
                    visited[ny][nx] = True
    if len(group) > 1:
        total_group.append((group, sum([A[y][x] for y, x in group]) // len(group)))
    else:
        visited[r][c] = False


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cnt = 0

while True:
    visited = [[False for c in range(N)] for r in range(N)]
    total_group = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs(r, c)
    if total_group:
        cnt += 1
        for each in total_group:
            for r, c in each[0]:
                A[r][c] = each[1]
    else:
        break

print(cnt)
