import sys

sys.stdin = open("최소이동거리_input.txt", "r")

import heapq


def path(start):
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        D, u = heapq.heappop(heap)

        # visited가 필요없는 방식
        # 현재 u까지의 최소거리가 D보다 작다는 것은 이미 이전에 u를 업데이트 했다는 의미: continue
        if dist[u] < D:
            continue
        
        for v in adj_list[u]:
            if D + v[1] < dist[v[0]]:
                dist[v[0]] = D + v[1]
                heapq.heappush(heap, (dist[v[0]], v[0]))

    return dist[N]

t = int(input())
for test_case in range(t):
    N, E = map(int, input().split())
    # 인접 리스트를 이용
    adj_list = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))

    INF = int(1e9)
    # 해당 노드까지 가는 데 필요한 최소 비용
    dist = [INF]*(N+1)
    heap = []
    print('#' + str(test_case + 1), path(0))