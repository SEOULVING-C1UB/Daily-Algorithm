import sys

sys.stdin = open("최소비용_input.txt", "r")

import heapq


def path(start):
    cost[start[0]][start[1]] = 0
    heapq.heappush(heap, (cost[start[0]][start[1]], (start[0], start[1])))

    while heap:
        C, u = heapq.heappop(heap)
        visited[u[0]][u[1]] = 1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        # 현재 노드에서 상하좌우를 체크
        for i in range(4):
            nx = u[0] + dx[i]
            ny = u[1] + dy[i]
            # 먼저 밖으로 나가지 않는지 체크
            if 0 <= nx < n and 0 <= ny < n:
                # 이동할 노드가 더 높다면 비용 높이차를 더함
                if heights[nx][ny] > heights[u[0]][u[1]]:
                    # 이동할 노드에 갱신해줄 비용: 현재까지 비용 + 높이차 + 기본 비용
                    n_cost = C + (heights[nx][ny] - heights[u[0]][u[1]] )+ 1
                else:
                    n_cost = C + 1
                # 이동할 노드에 방문한 적 없다면 비용 갱신하고 힙에 추가
                if not visited[nx][ny] and cost[nx][ny] > n_cost:
                    cost[nx][ny] = n_cost
                    heapq.heappush(heap, (cost[nx][ny], (nx, ny)))
    # 목적지까지의 비용 반환
    return cost[n-1][n-1]
    

t = int(input())
for test_case in range(t):
    n = int(input())
    heights = [list(map(int, input().split())) for _ in range(n)]
    INF = int(1e9)

    # 해당 노드까지 가는 데 필요한 최소 비용
    cost = [[INF]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    heap = []
    print('#' + str(test_case + 1), path((0, 0)))