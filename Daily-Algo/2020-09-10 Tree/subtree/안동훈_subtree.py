import sys
sys.stdin = open('subtree_input.txt')

# 노드 n에서부터 시작하며 전위 순회를 돌리면 쉽게 해결 가능할 것으로 보임

def pre_order(node):
    global answer
    if node == 0:
        return
    answer += 1
    if nodes[node][0] != 0:
        try:
            pre_order(nodes[node][0])
            pre_order(nodes[node][1])
        except:
            pass
    else:
        return


T = int(input())
for test_case in range(1, T + 1):
    answer = 0

    e, n = map(int, input().split()) # 간선의 개수 e, n을 root로 하는 서브트리의 크기 구하기
    edges = list(map(int, input().split()))
    nodes = [[0, 0] for _ in range(e+2)] # node들의 자식을 담을 배열

    for i in range(0, len(edges), 2):
        if not nodes[edges[i]][0]: # 왼쪽 자식이 없으면
            nodes[edges[i]][0] = edges[i+1]
        else: # 이미 자식이 존재하면 오른쪽 자식에 넣기
            nodes[edges[i]][1] = edges[i+1]

    pre_order(n) # 순회를 돌려보자.

    print("#{0} {1}".format(test_case, answer))