import sys

sys.stdin = open('이진탐색.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    # i: 노드 번호, nodes: 노드 트리
    i = 1
    nodes = [0] * (N + 1)

    # 1번 노드부터 순차적으로 값을 저장
    def tree(n):
        global i

        # n > N 이면 노드가 존재하지 않으므로 return
        if n > N:
            return

        # 왼쪽 자식 노드부터 값 저장
        tree(n * 2)

        # 자기 자신 저장 & 노드 번호 1 증가
        nodes[n] = i
        i += 1

        # 오른쪽 자식 노드 값 저장
        tree(n * 2 + 1)

    tree(1)

    print('#{} {} {}'.format(t, nodes[1], nodes[N // 2]))
