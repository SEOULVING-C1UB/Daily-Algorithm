N = int(input())
houses = [list(map(int, input())) for _ in range(N)]
# cpls : (list) store complexes of houses
cpls = []
visited = [[0 for i in range(N)] for j in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for j in range(N):
    for i in range(N):
        # check house or not
        if not houses[j][i]:
            continue

        # check visited or not
        if visited[j][i]:
            continue

        # cnt : (int) number of houses in this complex
        cnt = 1
        q = [(j, i)]
        visited[j][i] = 1
        while q:
            y, x = q.pop()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if houses[ny][nx] and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = 1
                        cnt += 1
        cpls.append(cnt)
print(len(cpls))
for c in sorted(cpls):
    print(c)
