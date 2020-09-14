N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

cnt = 0
ans = []


def check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def find(x, y):
    global cnt
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]
    if arr[x][y] == 1:
        visit[x][y] = 1
        for d in range(4):
            if check(x+delta_x[d], y+delta_y[d]) and arr[x + delta_x[d]][y + delta_y[d]] == 1 and visit[x + delta_x[d]][y + delta_y[d]] == 0:
                cnt += 1
                visit[x + delta_x[d]][y + delta_y[d]] = 1
                find(x+delta_x[d], y+delta_y[d])


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visit[i][j] == 0:
            cnt = 1
            find(i, j)
            if cnt != 0:
                ans.append(cnt)
        cnt = 0

for i in range(len(ans)):
    for j in range(len(ans)-i-1):
        if ans[j] > ans[j+1]:
            ans[j+1], ans[j] = ans[j], ans[j+1]

print(len(ans))
for i in ans:
    print(i)
