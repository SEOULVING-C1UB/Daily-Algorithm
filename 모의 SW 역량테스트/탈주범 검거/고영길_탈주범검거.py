from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
tournal = [0, (0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2), (0, 2)]
opp = [1, 0, 3, 2]

for tc in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[R][C] = 1
    cnt = 1
    cur_time = 1
    q = deque([(R, C)])
    while cur_time < L:
        cur_time += 1
        l = len(q)
        while l:
            l -= 1
            y, x = q.popleft()
            for d in tournal[MAP[y][x]]:
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < M:
                    if MAP[ny][nx] and not visited[ny][nx] and opp[d] in tournal[MAP[ny][nx]]:
                        cnt += 1
                        visited[ny][nx] = 1
                        q.append((ny, nx))
    print('#{} {}'.format(tc + 1, cnt))
