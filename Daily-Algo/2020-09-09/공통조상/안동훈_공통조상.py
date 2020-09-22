import sys
sys.stdin = open('공통조상_input.txt')

def post_order(node):
    global answer
    if node <= v:
        if nodes[node][0] != 0:
            post_order(nodes[node][0])
        if nodes[node][1] != 0:
            post_order(nodes[node][1])
        answer += 1

T = int(input())
for test_case in range(1, T + 1):
    answer = 0

    v, e, a, b = map(int, input().split())
    edges = list(map(int, input().split()))
    nodes = [[0, 0 ,0] for _ in range(v+1)] # node들의 left, right, parent를 담는 배열

    for i in range(0, len(edges), 2):
        nodes[edges[i+1]][2] = edges[i] # 부모 담기
        if nodes[edges[i]][0] == 0: # 왼쪽 자식이 없으면 담기
            nodes[edges[i]][0] = edges[i+1]
        else: # 왼쪽 자식이 있으면 오른쪽에 담기
            nodes[edges[i]][1] = edges[i+1]

    # a와 b의 조상 리스트를 찾는다.
    a_list = []
    b_list = []
    while True:
        if nodes[a][2] == 0:
            break
        a_list.append(nodes[a][2])
        a = nodes[a][2]
    while True:
        if nodes[b][2] == 0:
            break
        b_list.append(nodes[b][2])
        b = nodes[b][2]

    # 공통 조상 찾기
    common_value = 0
    for a_value in a_list:
        if a_value in b_list:
            common_value = a_value
            break

    # 공통 조상으로부터 후위 순회를 돌려 크기를 구한다.
    post_order(common_value)

    print("#{0} {1} {2}".format(test_case, common_value, answer))