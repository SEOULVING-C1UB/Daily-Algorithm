T = int(input())

for t in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    tmp = list(map(int, input().split()))
    # 트리를 생성합니다.
    # 생성 시 부모 노드에 자식 노드의 참조를 할당하고
    # 자식 노드에도 부모 노드의 참조 정보를 할당합니다.
    tree = [[0] * 3 for _ in range(V + 1)]
    for i in range(E):
        p = tmp[2 * i];
        c = tmp[2 * i + 1]
        if tree[p][0] == 0:     # 왼쪽 먼저
            tree[p][0] = c
        else:
            tree[p][1] = c      # 왼쪽에 없으면 오른쪽에 할당
        tree[c][2] = p          # 자식 노드에 부모요소 할당

    # 먼저 점검해야 하는 노드 중 1가지의 부모,조상노드를 리스트로 만듭니다.
    check = []
    parent = tree[N1][2]
    while parent:               # parent가0노드가 될떄까지 반복
        check.append(parent)
        parent = tree[parent][2]
    # 다음으로 위에서 구한 check list를 가지고
    # 남은 노드의 부모, 조상 노드 중 check list에 존재하는 노드를 구합니다.
    # 가장 먼저 발견되는 것이 가까운 노드입니다.
    parent = tree[N2][2]
    while parent:
        if parent in check:
            ans = parent
            parent = 0      # 발견하자마자 break를 거는 효과를 가집니다.
        else:
            parent = tree[parent][2]

    # 전위탐색으로 cnt를 더해 subtree의 크기를 구해줍니다.
    cnt = 0
    def preorder(s):
        global cnt
        if s == 0:
            return
        else:
            cnt += 1
            preorder(tree[s][0])
            preorder(tree[s][1])

    preorder(ans)
    print('#{} {} {}'.format(t, ans, cnt))