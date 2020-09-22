import sys
sys.stdin = open('노드의_합.txt')

T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)

    # 리트 노드 값 넣기
    for _ in range(M):
        index, value = map(int, input().split())
        nodes[index] = value

    def node(n):
        # 노드가 존재하지 않을 때
        if n > N:
            return 0

        # 이미 값이 있을 때
        if nodes[n]:
            return nodes[n]

        # 자기 자신 값은 왼쪽 자식 노드와 오른쪽 자식 노드의 합
        sum_value = node(n * 2) + node(n * 2 + 1)
        # nodes 리스트에 반영하고
        nodes[n] = sum_value

        # 자기 자신 값 return
        return sum_value

    node(1)

    print('#{} {}'.format(t, nodes[L]))
