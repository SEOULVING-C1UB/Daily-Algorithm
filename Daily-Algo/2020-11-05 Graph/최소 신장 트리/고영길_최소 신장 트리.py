import heapq

# prim
for tc in range(int(input())):
    V, E = map(int, input().split())
    V += 1
    MAP = {i: [] for i in range(V)}
    for i in range(E):
        s, e, c = map(int, input().split())
        MAP[s].append((e, c))
        MAP[e].append((s, c))
    INF = float('inf')
    key = [INF] * V
    key[0] = 0
    mst = [0] * V
    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        k, node = heapq.heappop(pq)
        if mst[node]:
            continue
        mst[node] = 1
        for dest, wt in MAP[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
    print('#{} {}'.format(tc + 1, sum(key)))


# kruskal
def find_set(n):
    if set_id[n] == n:
        return n
    else:
        set_id[n] = find_set(set_id[n])
        return set_id[n]


def union(v1, v2):
    p1, p2 = find_set(v1), find_set(v2)
    if rank[p1] > rank[p2]:
        set_id[p2] = set_id[p1]
    else:
        set_id[p1] = set_id[p2]
        if rank[p1] == rank[p2]:
            rank[p2] += 1


def mst():
    cnt = 0
    total = 0

    for i in range(E):
        p1, p2 = find_set(edges[i][0]), find_set(edges[i][1])
        if p1 != p2:
            total += edges[i][2]
            cnt += 1
            union(p1, p2)
        if cnt == V - 1:
            return total


for tc in range(int(input())):
    V, E = map(int, input().split())
    V += 1
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    set_id = [i for i in range(V)]
    rank = [0] * V
    print('#{} {}'.format(tc + 1, mst()))
