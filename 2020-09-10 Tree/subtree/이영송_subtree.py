import sys
sys.stdin = open('(5174)subtree_input.txt','r')

T = int(input())

for t in range(1,T+1):
    E,N = map(int,input().split())
    tmp = list(map(int,input().split()))
    # 배열을 선언하기 위해 노드의 개수를 max로 가져옵니다.
    S = max(tmp)
    # 부모/자식 노드 정보만 저장하고, index값으로 node 번호를 대체합니다
    tree = [[0]*2 for _ in range(S+1)]
    # tree 안에 parent,child를 저장하되, 왼쪽 child부터 저장해줍니다.
    # 만약 왼쪽이 차 있는 경우에만 오른쪽 child를 저장합니다.
    for i in range(E):
        p = tmp[2*i]
        c = tmp[2*i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    cnt = 0
    # 전위 순회를 사용합니다.
    def preorder(s):
        global cnt
        # 받아온 node의 값이 어디로도 갈 수 없을 때 기저점을 만들어 둡니다.
        # 그 떄에도 cnt +1을 해줍니다.
        if tree[s][0]==0 and tree[s][1] ==0:
            cnt += 1
            return
        else:
            # 위에서 검사해서 둘 중 하나라도 자식을 가지고 있는 경우에
            # 해당 노드를 방문하여 cnt 를 증가시킵니다.
            cnt += 1
            # 왼쪽 자식이 있는 경우 거기로 방문합니다.
            if tree[s][0] != 0:
                preorder(tree[s][0])
            # 오른쪽 자식이 있는 경우 거기도 방문합니다.
            if tree[s][1] != 0:
                preorder(tree[s][1])
    # N을 루트로 전위 순회를 시작합니다.
    preorder(N)
    # cnt를 출력합니다.
    print('#{} {}'.format(t,cnt))