from collections import deque


def find_set(y, x):
    if set_id[y][x] == y * N + x:
        return y * N + x
    else:
        set_id[y][x] = find_set(set_id[y][x] // N, set_id[y][x] % N)
        return set_id[y][x]


def union(y1, x1, y2, x2):
    g1 = find_set(y1, x1)
    g2 = find_set(y2, x2)
    set_id[g2 // N][g2 % N] = set_id[g1 // N][g1 % N]


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0]
dx = [0, 1]
cnt = 0

while True:
    set_id = [[r * N + c for c in range(N)] for r in range(N)]
    visited = [[False for c in range(N)] for r in range(N)]
    can_move = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            visited[r][c] = 1
            q = deque([(r, c)])
            while q:
                y, x = q.popleft()
                visited[y][x] = True
                for d in range(2):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if L <= abs(A[ny][nx] - A[y][x]) <= R:
                            if find_set(ny, nx) != find_set(r, c):
                                union(r, c, ny, nx)
                                can_move = True
                            q.append((ny, nx))
    if not can_move:
        break
    cnt += 1

    dict_groups = {}
    for r in range(N):
        for c in range(N):
            if set_id[r][c] in dict_groups:
                dict_groups[set_id[r][c]].append((r, c))
            else:
                dict_groups[set_id[r][c]] = [(r, c)]

    for group in dict_groups:
        if len(dict_groups[group]) == 1:
            continue
        population = sum([A[r][c] for r, c in dict_groups[group]]) // len(dict_groups[group])
        for r, c in dict_groups[group]:
            A[r][c] = population
    print(*set_id, sep='\n')
    print()
    print(*A, sep='\n')
    print()
print(cnt)
