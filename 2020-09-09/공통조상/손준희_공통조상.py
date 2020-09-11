def cal_node_count(node):   # node를 root node로 하는 서브트리의 노드 총 개수 구하는 재귀함수
    if not node[0] and not node[1]:     # 자식 없으면 1개
        return 1
    elif not node[0]:
        return cal_node_count(tree_graph[node[1]]) + 1
    elif not node[1]:
        return cal_node_count(tree_graph[node[0]]) + 1
    else:
        return cal_node_count(tree_graph[node[0]]) + cal_node_count(tree_graph[node[1]]) + 1


testcase = int(input())
for TC in range(testcase):
    V, E, child1, child2 = map(int, input().split())
    edges = list(map(int, input().split()))
    tree_graph = [[0, 0, 0] for i in range(V + 1)]      # 왼쪽자식, 오른쪽자식, 부모
    for i in range(0, 2 * E, 2):
        if not tree_graph[edges[i]][0]:     # 왼쪽자식 없으면 왼쪽에 자식 추가
            tree_graph[edges[i]][0] = edges[i + 1]
        else:                               # 있으면 오른쪽에 자식 추가
            tree_graph[edges[i]][1] = edges[i + 1]
        tree_graph[edges[i + 1]][2] = edges[i]      # 자식에게 부모를 알려주기
    ancestors = []  # 조상을 담을 빈 list
    i = child1
    while tree_graph[i][2]:     # 부모가 있는 동안에 순회한다
        ancestors.append(tree_graph[i][2])  # 현재 노드의 부모를 조상 list에 추가
        i = tree_graph[i][2]    # 현재 노드의 부모로 노드 변경
    i = child2
    while tree_graph[i][2]:     # 부모가 있는 동안에 순회한다
        if tree_graph[i][2] in ancestors:   # 현재 노드의 부모가 조상 list에 있으면 공통조상이므로 탈출
            break
        i = tree_graph[i][2]
    ancestor = tree_graph[i][2] # 탈출 당시의 노드의 부모를 기준으로 서브트리의 노드 개수 구하기
    print('#{} {} {}'.format(TC + 1, ancestor, cal_node_count(tree_graph[ancestor])))
