import sys

sys.stdin = open('회전.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    for _ in range(M):
        a = Q.pop(0)
        Q.append(a)
    print(Q[0])