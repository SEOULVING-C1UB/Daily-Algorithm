for t in range(1, 11):
    N = int(input())

    result = ''
    nodes = [0] * (N + 1)

    # nodes 리스트에 노드값들 반영
    for _ in range(N):
        node = input().split()
        nodes[int(node[0])] = node[1]

    # n: 현재 노드
    def tree(n):
        global result

        # 범위를 벗어났을 때
        if n > N:
            return

        # 왼쪽 서브 트리
        tree(n * 2)
        # 현재 노드 추가
        result += nodes[n]
        # 오른쪽 서브 트리
        tree(n * 2 + 1)

    tree(1)

    print('#{} {}'.format(t, result))
