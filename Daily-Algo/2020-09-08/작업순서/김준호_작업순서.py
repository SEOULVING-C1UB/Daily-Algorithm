import collections
import sys
sys.stdin = open('input.txt', 'r')

T = 10

def bfs():
    # pop(0)보다 popleft()가 시간 복잡도가 훨씬 낮기 떄문에 데크 사용
    queue = collections.deque()
    for i in range(1, v + 1):
        if before[i] == 0:
            queue.append(i)
    # 큐가 비면 끝
    while queue:
        # FIFO 후 출력
        cur = queue.popleft()
        print(cur, end=' ')
        # 인접한 노드의 선행조건을 차감 후 선행조건을 만족한 노드를 큐에 추가
        for adj in range(1, v + 1):
            if graph[cur][adj] == 1:
                before[adj] -= 1
                if before[adj] == 0:
                    queue.append(adj)


for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    visited = [0] * (v + 1)
    edges = list(map(int, input().split()))
    graph = [[0] * (v + 1) for _ in range(v + 1)]
    # 남은 선행조건 리스트
    before = [0] * (v + 1)
    # 그래프 생성, 선행조건 리스트 채우기
    for i in range(0, 2 * e, 2):
        graph[edges[i]][edges[i + 1]] = 1
        before[edges[i + 1]] += 1
    print('#{}'.format(test_case), end=' ')
    bfs()
    print()