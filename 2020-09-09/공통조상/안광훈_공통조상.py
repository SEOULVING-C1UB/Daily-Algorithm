T = int(input())

for t in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    edges = list(map(int, input().split()))

    # v1_parents: 첫 번째 노드의 부모 노드들 리스트
    v1_parents = []
    vertexes = [[0, 0, 0] for _ in range(V + 1)]

    # [왼쪽 자식, 오른쪽 자식, 부모 노드] 형식으로 vertexes에 추가
    for i in range(0, len(edges), 2):
        e1 = edges[i]
        e2 = edges[i + 1]

        vertexes[e2][2] = e1

        if vertexes[e1][0] == 0:
            vertexes[e1][0] = e2
        else:
            vertexes[e1][1] = e2

    # 첫 번째 노드 부모 노드들 추가
    while True:
        v1_parents.append(vertexes[v1][2])
        v1 = vertexes[v1][2]

        # 1이 루트 노드이므로 1이면 break
        if v1 == 1:
            v1_parents.append(vertexes[v1][2])
            break

    # 두 번째 노드 부모 노드들 탐색
    while True:
        v2 = vertexes[v2][2]

        # 첫 번째 노드 부모 노드와 겹친다면 break
        if v2 in v1_parents:
            break

    # 서브 트리 개수 구하는 함수
    def sub_tree(k):
        # 자식 노드가 없는 경우
        if k == 0:
            return 0

        # 자신 + 왼쪽 서브 트리 + 오른쪽 서브 트리
        return 1 + sub_tree(vertexes[k][0]) + sub_tree(vertexes[k][1])

    # v2가 공통 조상 값인 상태이므로
    result = sub_tree(v2)

    print('#{} {} {}'.format(t, v2, result))
