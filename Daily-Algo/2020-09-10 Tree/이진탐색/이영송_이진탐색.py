import sys
sys.stdin = open('(5176)이진탐색_input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    # 노드의 번호를 순회할 인덱스 정보로 곧바로 사용했습니다
    # tree[1] 은 1번 노드에 해당하는 값을 읽어옵니다.
    tree = list(range(N+1))
    # 중위순회
    def inorder(s):
        # 순회 순서대로 cnt 값을 누적시키시 위해 global 선언을 합니다.
        global cnt
        # index를 node 번허로 읽으려면 error 예외처리를 꼭 해주어ㅑ 합니다.
        # indexing error를 방지합니다.
        if s > N : return
        else:
            # indexing error가 나지 않는다면, 왼쪽 child에 값이 있다면 호출합니다.
            if 2*s <=N:
                inorder(tree[2*s])
            # 중위 순회 순서로 방문한 지점에 cnt를 삽입하고 그 값을 +1 더해줍니다.
            tree[s] = cnt
            cnt += 1
            # 오른쪽 child가 indexing error가 나지 않으면 호출합니다.
            if 2*s+1 <=N:
                inorder(tree[2*s+1])
    cnt = 1
    # 항상 루트 노드는 1입니다.
    inorder(1)
    print("#{} {} {}".format(t,tree[1],tree[N//2]))