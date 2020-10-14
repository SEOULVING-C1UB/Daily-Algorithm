from copy import deepcopy
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def cnt_iceberg():
    global h
    visited = [[0 for i in range(M)] for j in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(M):
            if not ice[j][i] or visited[j][i]:
                continue

            cnt += 1
            if cnt > 1:
                return cnt
            visited[j][i] = 1
            q = [(j, i)]
            while q:
                y, x = q.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M:
                        if ice[ny][nx] and not visited[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = 1

    if not cnt:
        h = 0
    return cnt


def melt(ice):
    after = deepcopy(ice)
    for j in range(N):
        for i in range(M):
            if ice[j][i]:
                cnt = 0
                for d in range(4):
                    if not ice[j + dy[d]][i + dx[d]]:
                        cnt += 1
                if ice[j][i] > cnt:
                    after[j][i] -= cnt
                else:
                    after[j][i] = 0
    return after



N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
h = 1

ice = melt(ice)
while cnt_iceberg() == 1:
    ice = melt(ice)
    h += 1


print(h)
