import sys

sys.stdin = open('subtree.txt')

T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    nodes = dict()

    # [왼쪽 자식 노드, 오른쪽 자식 노드] 형태로 저장
    for i in range(1, E + 2):
        nodes[i] = [0, 0]

    for i in range(0, len(edges), 2):
        parent_node = edges[i]
        child_node = edges[i + 1]

        # 왼쪽 자식이 없을 경우 왼쪽 자식에 저장
        if not nodes[parent_node][0]:
            nodes[parent_node][0] = child_node
        # 있을 경우 오른쪽 자식에 저장
        else:
            nodes[parent_node][1] = child_node


    def sub_tree(k):
        # k가 0이라는 건 노드가 존재하지 않는다는 의미 => 0 리턴
        if k == 0:
            return 0

        # 1 (자기 자신) + 왼쪽 서브 트리 + 오른쪽 서브 트리
        return 1 + sub_tree(nodes[k][0]) + sub_tree(nodes[k][1])


    result = sub_tree(N)

    print('#{} {}'.format(t, result))
