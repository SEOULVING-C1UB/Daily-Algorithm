import sys
N = int(input())
page = [[0] * 100 for _ in range(100)]  # 100 x 100 빈리스트

for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    for p in range(10):             # 가로, 세로 10 씩 증가하며 1 증가
        for q in range(10):
            page[x+p][y+q] += 1

ans = 0
for i in range(100):
    for j in range(100):
        if page[i][j] != 0:         # 0이 아닌 값은 모두 색칠된곳
            ans += 1
print(ans)
