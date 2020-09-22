# t: 테스트 케이스 번호
for t in range(1, 11):
    # N: 데이터의 길이, S: 시작점
    N, S = map(int, input().split())
    # data: 비상연락망 나열한 리스트
    data = list(map(int, input().split()))

    # contact: 간선 나타내는 딕셔너리
    contact = dict()

    # 각 노드를 key로 하고 value를 []로 초기화
    for i in range(1, 101):
        contact[i] = []

    # visited: 방문 체크 리스트
    visited = [0] * 101

    # 간선 contact 딕셔너리에 반영
    for i in range(0, N, 2):
        contact[data[i]].append(data[i + 1])


    def who_is_last(nodes):
        # 다음에 방문할 노드들
        new_nodes = []
        for node in nodes:
            for _node in contact[node]:
                if not visited[_node]:
                    visited[_node] = 1
                    new_nodes.append(_node)

        # 다음에 방문할 노드들이 없을 경우
        if not len(new_nodes):
            # 가장 큰 숫자를 반환
            return max(nodes)

        return who_is_last(new_nodes)


    result = who_is_last([S])
    print('#{} {}'.format(t, result))
