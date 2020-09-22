for t in range(1, 11):
    # V: 노드의 개수, E: 간선의 개수, edges: 간선 리스트
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    # result: 결과값, vertexes: 노드별 간선 딕셔너리, visited: 방문 체크 리스트
    result = []
    vertexes = dict()
    visited = [0] * (V + 1)

    for i in range(1, V + 1):
        vertexes[i] = set()

    # 간선 딕셔너리에 반영
    # 노드별 선행해야 하는 노드를 set로 가지고 있는 형식
    for i in range(0, len(edges), 2):
        vertexes[edges[i + 1]].add(edges[i])

    # 다 방문할 때까지
    while len(result) < V:
        # 이번에 방문할 노드
        cur_index = 0
        for j in range(1, V + 1):
            # 방문 체크 & 선행해야 하는 노드가 없다면 방문
            if not visited[j] and len(vertexes[j]) == 0:
                cur_index = j
                visited[j] = 1
                break
        result.append(str(cur_index))
        # 이번에 방문한 노드 선행 노드에서 제거
        for vertex in vertexes.values():
            vertex.discard(cur_index)

    print('#{} {}'.format(t, ' '.join(result)))
