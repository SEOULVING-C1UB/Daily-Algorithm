dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def find_safe_zone(h):
    cnt = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for j in range(N):
        for i in range(N):
            if field[j][i] <= h or visited[j][i]:
                continue

            visited[j][i] = 1
            cnt += 1
            q = [(j, i)]
            while q:
                y, x = q.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        if field[ny][nx] > h and not visited[ny][nx]:
                            q.append((ny,nx))
                            visited[ny][nx] = 1
    return cnt

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
height_set = set()
for j in range(N):
    for i in range(N):
        height_set.add(field[j][i])

answer = 1
for height in height_set:
    answer = max(answer, find_safe_zone(height))

print(answer)