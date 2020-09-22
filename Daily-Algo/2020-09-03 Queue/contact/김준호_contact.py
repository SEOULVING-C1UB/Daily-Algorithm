import sys
from collections import defaultdict
import heapq

sys.stdin = open("input.txt", "r")

T = 10

def bfs(start):
    # 시작점의 거리는 0
    distance[start] = 0
    queue = []
    # 우선순위 큐에 [거리, 시작점] 추가
    heapq.heappush(queue, [distance[start], start])

    while queue:
        # 현재 노드의 거리, 노드
        cur_dis, cur_node = heapq.heappop(queue)
        # 이미 저장된 거리가 더 작다면 다음으로
        if cur_dis > distance[cur_node]:
            continue
        # 인접 노드 탐색
        for adj in graph[cur_node]:
            # 다음 노드의 거리는 1 더 큰 값
            dis = cur_dis + 1
            # 미리 저장된 거리가 더 크다면 업데이트 후 힙큐에 추가
            if dis < distance[adj]:
                distance[adj] = dis
                heapq.heappush(queue, [dis, adj])
    return

for test_case in range(1, T + 1):
    n, start = map(int, input().split())
    connect = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(0, n, 2):
        graph[connect[i]].append(connect[i+1])
    # 모든 노드의 기본 거리값을 무한으로 설정
    distance = {node: float('inf') for node in connect}
    bfs(start)
    # 변화된 거리 값들을 무한값은 제거하고, 거리,노드값 역순으로 정렬
    call_list = sorted(filter(lambda x: x[1] != float('inf'), distance.items()), reverse=True, key=lambda x: (x[1],x[0]))
    # 거리가 가장 멀면서 노드가 제일 큰 값을 출력
    print('#{} {}'.format(test_case, call_list[0][0]))