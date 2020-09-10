import collections
import sys
sys.stdin = open('s_input.txt', 'r')
T = int(input())

# 연결된 곳을 모두 탐색, 방문처리
def dfs(start):
    need_visit = [start]
    while need_visit:
        cur = need_visit.pop()
        visited.append(cur)
        for adj in graph[cur]:
            if adj not in visited:
            	need_visit.append(adj)


for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = collections.defaultdict(list)
    visited = []
    count = 0
    # 그래프 생성(서로 연결되게)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 방문하지 않은 노드라면 탐색, 무리 + 1
    for i in range(1, n+1):
        if i not in visited:
            dfs(i)
            count += 1
    print('#{} {}'.format(test_case, count))
