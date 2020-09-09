import sys

sys.stdin = open('공통조상.txt', 'r')
T = int(input())
for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    V, E, N1, N2 = map(int, input().split())
    arr = list(map(int, input().split()))


    left = [0] * (V + 1)
    right = [0] * (V + 1)
    parent = [0] * (V + 1)
    visited = [0] * (V + 1)

    for i in range(0, 2 * E, 2):
        F = arr[i]
        S = arr[i + 1]
        if left[F] == 0:
            left[F] = S
        elif left[F] != 0:
            right[F] = S
        parent[S] = F

    L1, L2 = [], []

    p = -1
    s = N1
    while p != 0:
        p = parent[s]
        L1.append(p)
        s = p
    p = -1
    s = N2
    while p != 0:
        p = parent[s]
        L2.append(p)
        s = p
    result = []
    for v1 in L1:
        for v2 in L2:
            if v1 == v2:
                result.append(v2)
                break
    common = result[0]
    print(common, end=" ")


    s = []
    root = common
    while len(s) != V:
        if visited[root] == 0:
            s.append(root) # 스택에 루트 추가
        visited[root] = 1 # 방문 표시

        l = left[root]
        r = right[root]
        if l != 0 and visited[l] == 0:
            root = l
        elif visited[l] != 0 and r != 0 and visited[r] == 0:
            root = r
        elif (l == 0 or visited[l] != 0) and (r == 0 or visited[r] != 0):
            root = parent[root]
        if root == parent[common]:
            break
    print(len(s))




