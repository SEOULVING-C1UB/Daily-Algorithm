# t: 테스트 케이스 번호
for t in range(1, 11):
    # N: 총 노드 개수
    N = int(input())

    nodes = [0] * (N + 1)
    operators = ['+', '-', '*', '/']

    # 숫자일 경우 [노드 value] 형태로 저장
    # 연산 기호일 경우 [노드 value, 왼쪽 자식 노드, 오른쪽 자식 노드] 형태로 저장
    for _ in range(N):
        node_info = input().split()
        nodes[int(node_info[0])] = node_info[1:]

    def calculate(n):
        node = nodes[n][0]

        # 연산 기호일 경우
        if node in operators:
            node1 = int(nodes[n][1])
            node2 = int(nodes[n][2])
            if node == '+':
                return calculate(node1) + calculate(node2)
            if node == '-':
                return calculate(node1) - calculate(node2)
            if node == '*':
                return calculate(node1) * calculate(node2)
            if node == '/':
                return calculate(node1) / calculate(node2)

        # 숫자일 경우
        return int(node)

    result = int(calculate(1))

    print('#{} {}'.format(t, result))
