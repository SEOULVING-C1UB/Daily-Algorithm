
#조상 목록찾기
def findAncestor(n):

    current = tree[n][0]
    parent = []

    # 0이면 root니까 root가 아닐동안 부모들을 찾아낸다
    while current != 0:
        parent.append(current)
        current = tree[current][0]
        
    return parent


# 서브트리를 세기 위해서 트리를 만들면서 정점의 갯수를 세어줌
def preOrder(n):
    global cnt

    if n!= 0:
        cnt += 1
        preOrder(tree[n][1])
        preOrder(tree[n][2])


T = int(input())
for tc in range(1, T+1):

    V, E, a, b = map(int, input().split())

    # [parent, left, right]
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]

    tmp = list(map(int, input().split()))

    # 입력받은 노드들을 트리에 넣어줌
    for i in range(E):
        # 짝수 인덱스는 부모, 홀수 인덱스는 자식
        parent = tmp[i * 2]
        child = tmp[i * 2 + 1]

        # 왼쪽 오른쪽 상관없대니 그냥 들어오는 순서대로 자식을 넣어줬다
        if not tree[parent][1]:
            tree[parent][1] = child
        else:
            tree[parent][2] = child

        tree[child][0] = parent
        #tree 상태:[부모, 자식1, 자식2]

    pa = findAncestor(a)    #a의 부모 리스트
    pb = findAncestor(b)    #b의 부모 리스트

    common = 0      # 조상
    flag = 1        # 이중 for문이라 break용 flag
    # 제일 가까운 조상 찾기
    for i in range(len(pa)):
        if flag == 0:
            break
        for j in range(len(pb)):
            if pa[i] == pb[j]:
                common = pa[i]
                flag = 0
                break

    # print(tree)
    # print(pa, pb)


    cnt = 0     #트리 몇개인지 셀 거
    preOrder(common)
    print('#{} {} {}'.format(tc, common, cnt))
