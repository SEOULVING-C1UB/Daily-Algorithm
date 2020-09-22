import sys
sys.stdin = open('노드의_거리.txt')

# T: 테스트 케이스 개수
T = int(input())

# t: 테스트 케이스 번호
for t in range(1, T + 1):
    # V: 노드의 개수, E: 간선의 개수, graph: 그래프 딕셔너리
    V, E = map(int, input().split())
    graph = dict()

    # 모든 노드에 대해 value []으로 초기화
    for i in range(1, V+1):
        graph[i] = []

    # visited: 방문 체크 리스트
    visited = [0] * (V + 1)

    # 간선 graph에 반영
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    # S: 출발 노드, G: 도착 노드
    S, G = map(int, input().split())
    # S 방문 처리
    visited[S] = 1

    # k: 방문한 노드 개수, nodes: 방문할 노드 리스트
    def find_path(k, nodes):
        global V, G

        # 방문할 노드가 없다면 0 리턴
        if not len(nodes):
            return 0

        # 다음에 방문할 노드들
        new_nodes = []

        for node in nodes:
            for _node in graph[node]:
                # 도착했다면 k + 1 리턴
                if _node == G:
                    return k + 1

                if not visited[_node]:
                    visited[_node] = 1
                    new_nodes.append(_node)

        return find_path(k + 1, new_nodes)

    result = find_path(0, [S])
    print('#{} {}'.format(t, result))
