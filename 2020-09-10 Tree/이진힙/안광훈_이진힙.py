import sys

sys.stdin = open('이진_힙.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    nodes = [0]


    def add_node(node):
        # 일단 맨 마지막 노드에 추가
        nodes.append(node)

        # n: 현재 노드 번호
        n = len(nodes) - 1

        # n이 루트 노드가 아닐 경우
        while n > 1:
            # 부모보다 값이 클 경우 안 바꿔도 되므로 break
            if nodes[n] > nodes[n // 2]:
                break

            # 값이 작을 경우 부모 노드와 값 바꾸기
            nodes[n], nodes[n // 2] = nodes[n // 2], nodes[n]
            # 부모 노드 번호로 노드 번호 변경
            n //= 2


    for i in range(N):
        add_node(numbers[i])

    result = 0
    # 마지막 노드 번호
    m = len(nodes) - 1

    # 조상 노드가 루트 노드가 될 때까지
    while m > 1:
        m //= 2
        result += nodes[m]

    print('#{} {}'.format(t, result))
