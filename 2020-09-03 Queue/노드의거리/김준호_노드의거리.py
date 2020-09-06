import sys
from collections import defaultdict
import heapq
sys.stdin = open("노드의거리_input.txt", "r")

T = int(input())

# 다익스트라
def dijkstra(start):
    distance[start] = 0     # 시작점의 거리는 0
    queue = []              # 큐 생성
    heapq.heappush(queue, [distance[start], start])     # 우선순위 큐 => [거리, 노드] 
    while queue:
        cur_dis, cur_node = heapq.heappop(queue)        # 거리가 가장 작은 것을 꺼내옴
        if cur_node == g:   # 골에 도달 했다면 그 거리를 반환
            return cur_dis

        if distance[cur_node] < cur_dis:    # 이미 저장된 거리값이 더 작다면 다음 순서로
            continue
        
        for adj in graph[cur_node]: # 인접한 노드들 탐색
            dis = cur_dis + 1       # 거리 1 증가
            if dis < distance[adj]: # 저장된 거리보다 작다면
                distance[adj] = dis # 거리 업데이트
                heapq.heappush(queue, [dis, adj])   # 힙큐에 추가
    return 0    # 모두 탐색했는데 도달 못했다면 0 반환

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    # 그래프 만들기
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 모든 노드의 거리를 무한대로 딕셔너리 생성
    distance = {node: float('inf') for node in graph}
    s, g = map(int, input().split())
    print('#{} {}'.format(test_case, dijkstra(s)))