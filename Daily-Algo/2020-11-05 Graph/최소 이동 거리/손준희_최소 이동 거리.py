import collections


INF = 999999


for TC in range(int(input())):
    N, E = map(int, input().split())
    table = [[0] * (N + 1) for i in range(N + 1)]   # 인접행렬
    for i in range(E):
        edge = list(map(int, input().split()))
        table[edge[0]][edge[1]] = edge[2]
    mapping = [INF] * (N + 1)   # 0에서 1 ~ N까지 가는 데 필요한 cost
    mapping[0] = 0
    stack = collections.deque()
    stack.append((0, 0))
    while stack:
        p, cost = stack.popleft()
        for next_p in range(N + 1):
            if table[p][next_p]:    # p에서 next_p로의 길이 있을 때
                if mapping[next_p] > cost + table[p][next_p]:       # 0에서 next_p로 직접 가는 길의 거리가 더 크면
                    mapping[next_p] = cost + table[p][next_p]       # 거쳐가는 길을 맵핑한다.
                    if not next_p == N:     # N에 도달하지 않은 경우에만
                        stack.append((next_p, mapping[next_p]))     # 계속 stack에 추가한다.
    print('#{} {}' .format(TC+1, mapping[N]))

