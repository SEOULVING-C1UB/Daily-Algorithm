import sys
sys.stdin = open('(5178)노드의합_input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M, L = map(int,input().split())
    # 순회하기 위한 Tree를 생성
    tree = [[0]*3 for _ in range(N+1)]
    # 각 tree의 [1]은 해당 노드의 value
    # [0]은 왼쪽 child의 참조, [2]는 오른쪽 child의 참조
    for i in range(1,N+1):
        if 2*i <= N:
            tree[i][0] = 2*i
        if 2*i + 1 <= N:
            tree[i][2] = 2*i + 1
    # tree[node]에 value를 할당
    # tree[node]에는 [0,1,2]가 있으며, 1이 해당 node의 value
    for i in range(M):
        node, value = map(int,input().split())
        tree[node][1] = value
    # 후위순회
    def postorder(n):
        # 예외처리
        if n > N: return
        else:
            # n이 0이 아닐 때
            if n:
                # 후위순회 방문 순서, 왼쪽 , 오른쪽
                postorder(tree[n][0])
                postorder(tree[n][2])
                # 모든 후위 순회를 마친후 방문한 지점에 대하여 
                # 만약, 리프에 값이 있으면 넘어가고
                # 리프에 값이 0인 경우, child의 값을 더해줌
                # 이 때, list indexing error를 방지하기 위해
                # n*2와 n*2+1에 대하여 각각 예외처리하였음
                if tree[n][1] == 0 and n*2 <= N:
                    if n*2+1<=N:
                        tree[n][1] = tree[n*2][1] + tree[n * 2 + 1][1]
                    else:
                        tree[n][1] = tree[n*2][1]
    
    # tree root = 1
    postorder(1)
    # L번째의 값은 [1]로 인덱싱
    print('#{} {}'.format(t,tree[L][1]))