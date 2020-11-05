import heapq
import sys

sys.stdin = open('최소 이동 거리_input.txt', 'r')
for tc in range(int(input())):
    V, E = map(int, input().split())
    MAP = {i: [] for i in range(V + 1)}
    for _ in range(E):
        s, e, d = map(int, input().split())
        MAP[s].append((e, d))

    INF = float('inf')
    dist = [INF] * (V + 1)
    visited = [0] * (V + 1)
    dist[0] = 0
    q = [(dist[0], 0)]
    while q:
        cur_dist, node = heapq.heappop(q)
        visited[node] = 1
        for dest, wt in MAP[node]:
            if not visited[dest] and dist[dest] > cur_dist + wt:
                dist[dest] = cur_dist + wt
                heapq.heappush(q, (dist[dest], dest))
    print('#{} {}'.format(tc + 1, dist[-1]))
