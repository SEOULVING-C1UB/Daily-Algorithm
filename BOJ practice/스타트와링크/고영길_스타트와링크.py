from itertools import combinations as coms

N = int(input())
p = [list(map(int, input().split())) for j in range(N)]
answer = 1e9

for t1 in coms(range(N), N // 2):
    t2 = [i for i in range(N) if i not in t1]
    s1, s2 = 0, 0
    for i in range(N):
        if i in t1:
            for j in t1:
                s1 += p[i][j]
        else:
            for j in t2:
                s2 += p[i][j]
    answer = min(answer, abs(s1-s2))
print(answer)

