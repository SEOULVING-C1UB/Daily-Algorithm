import sys

sys.stdin = open('노드의 거리.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    mat = [[0] * V for _ in range(V)]
    print(mat)
    print(V, E)
    print(arr)
    print(S, G)