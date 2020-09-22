import sys

sys.stdin = open('피자 굽기.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    Ci = list(enumerate(Ci))
    Q = []
    for _ in range(N):
        Q.append(Ci.pop(0))
    while len(Q) != 1:
        p = Q.pop(0)
        if p[1] // 2 == 0:
            if len(Ci) != 0:
                Q.append(Ci.pop(0))
        else:
            Q.append((p[0], p[1] // 2))
    print(Q[0][0] + 1)

