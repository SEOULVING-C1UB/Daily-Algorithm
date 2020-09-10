T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    result = 0
    included = [0] * (N + 1)
    people = [[0] * (N + 1) for _ in range(N + 1)]

    # 인접 행렬 만들기
    for _ in range(M):
        p1, p2 = map(int, input().split())
        people[p1][p2] = 1
        people[p2][p1] = 1

    def grouping(k):
        for i in range(1, N + 1):
            # 연결되어 있으면 그룹에 추가
            if included[i] == 0 and people[k][i] == 1:
                included[i] = 1
                grouping(i)

    for j in range(1, N + 1):
        if included[j]:
            continue
        included[j] = 1
        grouping(j)
        result += 1

    print('#{} {}'.format(t, result))
